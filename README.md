
# YouTube Automation Script

This repository contains a simple automation script using Selenium with Python to automate the process of searching for and viewing a video on YouTube.

## Prerequisites

- Python 3.x installed on your machine.
- Selenium library installed. You can install it using pip:

  ```bash
  pip install selenium
  ```

- A web driver compatible with your browser (e.g., ChromeDriver for Google Chrome). Make sure the driver is in your system's PATH.

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the directory containing the script:

   ```bash
   cd <directory-name>
   ```

3. Open the script file and modify the video title in the search box line to the desired video you want to automate.

4. Run the script:

   ```bash
   python youtube_automation.py
   ```

## Script Overview

- The script opens a web browser and navigates to YouTube.
- It searches for a specified video title and clicks on the first video in the search results.
- The video plays for a specified duration before the browser closes.

## License

This project is licensed under the MIT License.
