# Bug-Scraper-Summarizer
Bugzilla, GNU and Debian Bugs Scrapped with playwright and summarized with GPT 4o-mini

# Bug Extraction and Summarization Automation

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

### **1. Clone the Repository**
```bash
git clone https://github.com/username/Bug-Extraction-Automation.git
cd Bug-Extraction-Automation

