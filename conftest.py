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

@pytest.fixture(scope="function")
def galaxy_s8_browser():
    with sync_playwright() as playwright:
        galaxy_s8 = playwright.devices['Nexus 5X']
        iphone_browser = playwright.webkit.launch(headless=False)
        context = iphone_browser.new_context(**galaxy_s8)
        yield context.new_page()
        iphone_browser.close()
