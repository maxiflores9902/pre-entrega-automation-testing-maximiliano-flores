import pytest
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
import time
import pathlib


target = pathlib.Path("reports/screens")
target.mkdir(parents=True, exist_ok=True)

@pytest.fixture
def base_url():
    return "https://reqres.in/api/users"

@pytest.fixture
def header_request():
    return {"x-api-key": "reqres-free-v1"}

@pytest.fixture
def driver(request):
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_driver(driver):
    LoginPage(driver).open_page()
    return driver

@pytest.hookimpl(hookwrapper=True)
def screen_make_report(item,call):
    outcome = yield
    report = outcome.get_result()
    if report.when in ("setup", "call") and report.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            timestamp_unix = int(time.time())
            file_name = target / f"{report.when}_{item.name}_{timestamp_unix}.png"
            driver.save_screenshot(file_name)
