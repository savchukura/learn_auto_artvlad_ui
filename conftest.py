import allure
from allure import attachment_type
from datetime import datetime
import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    #driver = webdriver.Chrome('/usr/bin/chromedriver')
    driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    #allure.attach('screenshot', driver.get_screenshot_as_png(), type=attachment_type.PNG)
    driver.quit()
