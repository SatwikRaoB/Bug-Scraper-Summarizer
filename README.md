# Bug-Scraper-Summarizer
Bugzilla, GNU and Debian Bugs Scrapped with playwright and summarized with GPT 4o-mini


## Overview
This project automates the extraction and summarization of bug reports from various bug tracking systems, including Bugzilla, Debian BTS, and GNU Bug Tracker. Using Playwright for web scraping and GPT-4 for summarization, the system collects raw bug data and transforms it into structured, concise summaries. The final output is stored in an organized format, such as Excel files, for easy interpretation and analysis.

---

## **Features**
- **Scraping**: 
  - Extracts bug information from dynamic and static web pages.
  - Supports Bugzilla, Debian BTS, and GNU Bug Tracker.
  - Handles JavaScript-heavy sites, paginated content, and structured HTML layouts.
  - Saves raw bug data in a structured `.txt` format.

- **Summarization**:
  - Processes raw bug data using GPT-4 for natural language summarization.
  - Extracts key details like bug descriptions, reproduction steps, classifications, and system-related information.
  - Stores the summarized data in Excel files.

---

## **Prerequisites**
- Python 3.8 or later
- Required Python libraries (see `requirements.txt`)

---

## **Steps to Execute**

1. **Clone the Repository**
    ```bash
    git clone https://github.com/username/Bug-Extraction-Automation.git
    cd Bug-Extraction-Automation
    ```

2. **Install Dependencies**
    Install the necessary Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**
    Create a `.env` file in the root directory with the following variables:
    ```env
    setx OPENAI_API_KEY="your_openai_api_key"
    ```

4. **Prepare Input Data**
    Place an Excel file containing bug URLs in the `data/` directory.
    Ensure the file follows this format:
    - **Bugzilla**: URLs listed in column A.
    - **Debian BTS**: URLs listed in column B.
    - **GNU Bug Tracker**: URLs listed in column C.

5. **Run Scraping Scripts**
    Execute the scraping scripts for each bug tracking system:
    ```bash
    python scraping/bugzilla_scraper.py
    python scraping/debian_scraper.py
    python scraping/gnu_scraper.py
    ```
    Scraped data is saved in `.txt` files in the `output/` directory.
    Errors, if any, are logged in the `logs/` directory.

6. **Run Summarization Script**
    Process the scraped data to generate summaries:
    ```bash
    python summarization/gpt4_summarizer.py
    ```
    Summarized data is saved in Excel format in the `output/` directory.

7. **Combine Summarized Data (Optional)**
    To generate a single Excel file with all summarized bug data:
    ```bash
    python utils/combine_output.py
    ```

8. **Review Output**
    Final outputs are stored in the `output/` directory.
    Open the Excel files to review the structured summaries of bug reports.

**Additional Notes**

- **Error Handling**: Logs can be found in the `logs/` directory to debug scraping or summarization issues.
- **Rate Limiting**: The system incorporates delays and retries to handle rate limits during scraping and summarization.
- **Batch Processing**: Processes large numbers of bug URLs in batches of 50 to ensure scalability.




