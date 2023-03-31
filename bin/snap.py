import os
import platform
import requests
import uuid
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from PIL import Image

# Get user input for the URL
url = input("Enter the URL to capture: ")

# Get browser choice from user
choice = input("Enter 1 to use Chrome, 2 to use Firefox, or 3 to use both: ")

# Set the path to the Snapshot folder
snapshot_folder = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'Snapshot'))

# Create the Snapshot folder if it does not exist
if not os.path.exists(snapshot_folder):
    os.mkdir(snapshot_folder)

# Delete previous screenshots
snapshot_folder = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "..", "Snapshot")
for file_name in os.listdir(snapshot_folder):
    file_path = os.path.join(snapshot_folder, file_name)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(f"Failed to delete {file_path}. Reason: {e}")

if choice == '1' or choice == '3':
    # Detect the installed Chrome version
    chrome_version = ''
    if platform.system() == 'Windows':
        output = os.popen(
            'reg query "HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon" /v version').read()
        chrome_version = output.split()[-1]
    elif platform.system() == 'Darwin':
        output = os.popen(
            'defaults read /Applications/Google\ Chrome.app/Contents/Info.plist CFBundleShortVersionString').read()
        chrome_version = output.strip()
    # Download the appropriate version of ChromeDriver
    if chrome_version:
        driver_url = f"https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{chrome_version.split('.')[0]}"
        response = requests.get(driver_url)
        if response.status_code == 200:
            driver_version = response.text.strip()
            driver_filename = f"chromedriver{''.join(platform.architecture())}"
            driver_url = f"https://chromedriver.storage.googleapis.com/{driver_version}/{driver_filename}.zip"
            driver_path = os.path.join(
                os.path.dirname(__file__), driver_filename)
            if not os.path.exists(driver_path):
                response = requests.get(driver_url)
                with open(driver_path + '.zip', 'wb') as f:
                    f.write(response.content)
                os.system(
                    f"unzip {driver_path}.zip -d {os.path.dirname(__file__)}")
                os.remove(driver_path + '.zip')
            chrome_driver_path = driver_path
        else:
            raise Exception(
                "Could not find appropriate version of ChromeDriver")
    else:
        raise Exception("Could not detect installed Chrome version")
    # Open Chrome and navigate to YouTube
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # enable headless mode
    options.add_argument('--start-maximized')  # maximize window
    options.add_argument('--window-size=1920x1080')  # set window size
    chrome_browser = webdriver.Chrome(chrome_driver_path, options=options)
    chrome_browser.get(url)
    sleep(5)
    chrome_screenshot = chrome_browser.get_screenshot_as_png()
    chrome_browser.quit()
    # Generate unique file names for the screenshots
    chrome_uuid = str(uuid.uuid4())
    chrome_save_path = os.path.join(
        snapshot_folder, f"chrome_screenshot_{chrome_uuid}.png")
    # Save the screenshots to files
    with open(chrome_save_path, "wb") as f:
        f.write(chrome_screenshot)

if choice == '2' or choice == '3':
    # Download latest version of geckodriver for Firefox
    response = requests.get(
        'https://github.com/mozilla/geckodriver/releases/latest')
    geckodriver_version = response.url.split('/')[-1]
    download_link = f'https://github.com/mozilla/geckodriver/releases/download/{geckodriver_version}/geckodriver-{geckodriver_version}-{"win" if os.name == "nt" else "macos"}.tar.gz'
    geckodriver_path = os.path.join(os.path.dirname(
        __file__), 'geckodriver.exe' if os.name == 'nt' else 'geckodriver')
    with open(geckodriver_path + '.tar.gz', 'wb') as f:
        f.write(requests.get(download_link).content)
    os.system(
        f'tar -xzf {geckodriver_path}.tar.gz -C {os.path.dirname(__file__)}')
    os.remove(f'{geckodriver_path}.tar.gz')
    # Open Firefox and navigate to YouTube
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')  # enable headless mode
    options.add_argument('--start-maximized')  # maximize window
    options.add_argument('--window-size=1920,1080')  # set window size
    options.add_argument('--force-device-scale-factor=0.75')
    firefox_browser = webdriver.Firefox(
        executable_path=geckodriver_path, options=options)
    firefox_browser.get(url)
    sleep(5)
    firefox_screenshot = firefox_browser.get_screenshot_as_png()
    firefox_browser.quit()
    # Generate unique file names for the screenshots
    firefox_uuid = str(uuid.uuid4())
    firefox_save_path = os.path.join(
        snapshot_folder, f"firefox_screenshot_{firefox_uuid}.png")
    # Save the screenshots to files
    with open(firefox_save_path, "wb") as f:
        f.write(firefox_screenshot)

