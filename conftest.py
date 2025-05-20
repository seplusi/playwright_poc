import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def chromium_browser():
    with sync_playwright() as playwright:
        chromium_browser = playwright.chromium # or "firefox" or "webkit".
        browser = chromium_browser.launch(args=['--start-maximized'], headless=False)
        page = browser.new_page(no_viewport=True)
        yield page
        browser.close()

@pytest.fixture(scope="function")
def firefox_browser():
    with sync_playwright() as playwright:
        chromium_browser = playwright.firefox # or "firefox" or "webkit".
        browser = chromium_browser.launch(args=['--start-maximized'], headless=False)
        page = browser.new_page(no_viewport=True)
        yield page
        browser.close()