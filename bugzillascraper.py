from playwright.sync_api import sync_playwright
import pandas as pd
import time
from tqdm import tqdm
import logging

# Setup logging
logging.basicConfig(filename='scraping_errors.log', level=logging.ERROR)

# Parse Excel file to get bug links
df = pd.read_excel('bugsmini.xlsx', sheet_name='Sheet1')
bug_links = df['LINK'].tolist()

# Function to scrape data from a URL using Playwright
def scrape_data(page, url):
    try:
        page.goto(url)
        page.wait_for_selector('div.bz_short_desc_container.edit_form', timeout=10000)
        page.wait_for_selector('td#bz_show_bug_column_1', timeout=10000)
        page.wait_for_selector('pre.bz_comment_text', timeout=10000)
        short_desc = page.inner_text('div.bz_short_desc_container.edit_form')
        bug_column = page.inner_text('td#bz_show_bug_column_1')
        comments = page.inner_text('pre.bz_comment_text')
        return {'short_desc': short_desc, 'bug_column': bug_column, 'comments': comments}
    except Exception as e:
        logging.error(f"Error scraping {url}: {e}")
        return None

# Break the bug links into batches of 50
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Start Playwright and use headless browser
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    total_start_time = time.time()  # Track total start time

    batch_number = 1
    total_links_processed = 0
    for batch in chunks(bug_links, 50):
        batch_start_time = time.time()  # Track batch start time
        
        scraped_data = {}
        for link in tqdm(batch, desc=f"Scraping Progress (Batch {batch_number})", unit="link"):
            scraped_data[link] = scrape_data(page, link)
            time.sleep(2)

        # Save the scraped data for each batch in a separate .txt file
        with open(f'scraped_data_batch_{batch_number}.txt', 'w', encoding='utf-8') as file:
            for link, content in scraped_data.items():
                if content:
                    file.write(f"LINK: {link}\n")
                    file.write(f"Short Description:\n{content['short_desc']}\n")
                    file.write(f"Bug Column:\n{content['bug_column']}\n")
                    file.write(f"Comments:\n{content['comments']}\n")
                    file.write("-" * 80 + "\n")

        batch_time_taken = time.time() - batch_start_time  # Calculate time taken for the batch
        print(f"Batch {batch_number} time taken: {batch_time_taken:.2f} seconds")

        total_links_processed += len(batch)
        batch_number += 1

    total_time_taken = time.time() - total_start_time  # Calculate total time taken
    average_time_per_url = total_time_taken / total_links_processed  # Calculate average time per URL

    # Close the browser when done
    browser.close()

print(f"Total time taken: {total_time_taken:.2f} seconds")
print(f"Average time per URL: {average_time_per_url:.2f} seconds")
