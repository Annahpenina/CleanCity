import os, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # optional: headless
    # chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def capture_screenshot(driver, name="screenshot"):
    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{name}_{int(time.time())}.png")
    driver.save_screenshot(path)
    print(f"✅ Screenshot saved: {path}")
