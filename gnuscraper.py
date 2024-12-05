import pandas as pd
from tqdm import tqdm
from playwright.sync_api import sync_playwright

def read_urls_from_excel(file_path):
    df = pd.read_excel(file_path, usecols=['LINK'], dtype=str)
    return df['LINK'].dropna().tolist()

def scrape_gnu_data(urls, start_index, end_index):
    scraped_data = []
    error_log = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for url in tqdm(urls[start_index:end_index], desc="Scraping URLs"):
            page.goto(url)
            page.wait_for_load_state("networkidle")  # Wait for the page to load completely

            try:
                # Extract the h1 element and get its inner HTML
                h1_element = page.query_selector("h1")
                if h1_element:
                    h1_inner_html = h1_element.inner_html()
                    # Split the inner HTML by <br> and take the second part if it exists
                    parts = h1_inner_html.split('<br>')
                    bug_description = parts[1].strip() if len(parts) > 1 else "No text after <br> found"
                else:   
                    bug_description = "No h1 found"

                pkginfo = page.query_selector("div.pkginfo").inner_text() if page.query_selector("div.pkginfo") else "No pkginfo found"
                buginfo = page.query_selector("div.buginfo").inner_text() if page.query_selector("div.buginfo") else "No buginfo found"

                # Find the first pre.message
                pre_messages = page.query_selector_all("pre.message")
                first_message = pre_messages[0].inner_text() if pre_messages else "No message found"

                # Ignore pre.mime and pre.headers
                if page.query_selector("pre.mime"):
                    mime_text = page.query_selector("pre.mime").inner_text()
                    first_message = first_message.replace(mime_text, "")
                if page.query_selector("pre.headers"):
                    headers_text = page.query_selector("pre.headers").inner_text()
                    first_message = first_message.replace(headers_text, "")

                # Format the data to include the bug description
                data = (f"Main URL: {url}\n"
                        f"Bug Description: {bug_description}\n"
                        f"PKGINFO:\n{pkginfo}\n\n"
                        f"BUGINFO:\n{buginfo}\n\n"
                        f"FIRST MESSAGE:\n{first_message}\n")
                scraped_data.append(data)
            except Exception as e:
                error_log.append(f"URL: {url}\nError: {e}\n")
                scraped_data.append(f"URL: {url}\nError: {e}\n")  # Append error to the scraped data as well

        browser.close()

    # Log errors to a separate file if any
    if error_log:
        with open('error_log.txt', 'w', encoding='utf-8') as error_file:
            for error in error_log:
                error_file.write(error + '\n')

    return scraped_data

def save_data_to_txt(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        for entry in data:
            file.write(entry + '\n' + ('='*80) + '\n')

def main():
    # Path to your Excel file
    excel_file_path = "GNUmini.xlsx"

    # Read URLs from Excel
    urls = read_urls_from_excel(excel_file_path)

    # Set the batch size
    batch_size = 50
    num_batches = len(urls) // batch_size + (1 if len(urls) % batch_size != 0 else 0)

    for batch_num in range(num_batches):
        start_index = batch_num * batch_size
        end_index = start_index + batch_size

        # Scrape data from URLs
        scraped_data = scrape_gnu_data(urls, start_index, end_index)

        # Save scraped data to a .txt file
        txt_file_path = f"scraped_gnu_data_batch_{batch_num + 1}.txt"
        save_data_to_txt(txt_file_path, scraped_data)

        print(f"Data saved to {txt_file_path}")

if __name__ == "__main__":
    main()
