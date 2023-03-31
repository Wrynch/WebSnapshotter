# WebSnapshotter
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![PyPI version](https://badge.fury.io/py/PACKAGE_NAME.svg)](https://badge.fury.io/py/PACKAGE_NAME)
![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10-blue)

WebSnapshotter is a Python script that takes screenshots of websites using the Chrome or Firefox browsers. It allows you to save the images to a specific folder and choose whether to take screenshots of a single browser or both.
Requirements

    Python 3.x
    Selenium: pip install selenium
    Chrome or Firefox browser installed

Installation

    Clone or download this repository to your computer.
    Install the required packages: pip install selenium.
    Run the script: python snap.py.

Usage

    When prompted, enter the URL of the website you want to take a screenshot of.
    Choose the browser(s) you want to use: Chrome, Firefox or both.
    Choose whether to accept cookies or not.
    The script will take a screenshot of the website and save it in the Snapshot folder in the parent directory of the WebSnapshotter folder.
    You can find the screenshot(s) with the name browsername_screenshot.png in the Snapshot folder.

## Libraries

 - [requests](https://pypi.org/project/requests/)
 - [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
 - [selenium](https://selenium-python.readthedocs.io/)
