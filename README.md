# Bug-Scraper-Summarizer
Bugzilla, GNU and Debian Bugs Scrapped with playwright and summarized with GPT 4o-mini

<br />



## Overview
This project automates the extraction and summarization of bug reports from various bug tracking systems, including Bugzilla, Debian BTS, and GNU Bug Tracker. Using Playwright for web scraping and GPT-4 for summarization, the system collects raw bug data and transforms it into structured, concise summaries. The final output is stored in an organized format, such as Excel files, for easy interpretation and analysis.

<br />


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

<br />


  ---

## **Prerequisites**
- Python 3.8 or later
- Required Python libraries (see `requirements.txt`)

<br />


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
    Get your OPENAI api key here: https://platform.openai.com/api-keys

4. **Prepare Input Data**
    Place an Excel file containing bug URLs in the `data/` directory.
    Ensure the file has "LINK" column with the respective url of the bug description.

5. **Run Scraping Scripts**
    Execute the scraping scripts for each bug tracking system:
    ```bash
    python bugzilla_scraper.py
    python gnu_scraper.py (run the same for debian website)
    ```
    Scraped data is saved in `.txt` files in the `output/` directory.
    Errors, if any, are logged in the `logs/` directory.

6. **Run Summarization Script**
    Process the scraped data to generate summaries:
    ```bash
    python summarizer.py
    ```
    Summarized data is saved in Excel format in the `output/` directory.

7. **Review Output**
    Final outputs are stored in the `output/` directory.
    Open the Excel files to review the structured summaries of bug reports.
   
<br />

  ---

**Additional Notes**

- **Error Handling**: Logs can be found in the `logs/` directory to debug scraping or summarization issues.
- **Rate Limiting**: The system incorporates delays and retries to handle rate limits during scraping and summarization.
- **Batch Processing**: Processes large numbers of bug URLs in batches of 50 to ensure scalability.




