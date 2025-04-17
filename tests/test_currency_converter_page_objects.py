import re
from playwright.sync_api import expect
from page_objects.currency_converter_convert_page import converPage

def test_currency_converter_page_chrome(chromium_browser):
    page = converPage(chromium_browser)
    page.navigate("https://www.xe.com/")
    
    # Accept cookie
    page.accept_cookie()

    # Expect a title "to contain" a substring.
    expect(page.page).to_have_title(re.compile("Currency Exchange Rates and International Money Transfers"))

    # Delete the default amount and type 100
    page.enter_amount("100")

    # Specify the source currency
    page.select_from_currency_brz()

    # Specify the destination currency
    page.select_to_currency_euro()
    
    # Click convert button
    page.convert_btn.click()
    page.convert_btn.is_hidden

    # Assert conversion result texts
    locator = page.page.get_by_test_id("conversion").get_by_text(re.compile("Brazilian Reais"))
    expect(locator).to_have_text('100.00 Brazilian Reais =')

    locator = page.page.get_by_test_id("conversion").locator("p").nth(1)
    expect(locator).to_have_text(re.compile("^[0-9]{2}.[0-9]{4,6} Euros$"))

    locator = page.page.get_by_test_id("conversion").locator("p").nth(2)
    expect(locator).to_have_text(re.compile("^1 BRL = 0.[0-9]{4,6} EUR$$"))

    locator = page.page.get_by_test_id("conversion").locator("p").nth(3)
    expect(locator).to_have_text(re.compile("^1 EUR = [0-9]{1}.[0-9]{4,6} BRL$"))

def test_currency_converter_page_firefox(firefox_browser):
    page = firefox_browser
    page.goto("https://www.xe.com/")
    # Accept cookie
    page.get_by_role("button").get_by_text("Accept").click()

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Currency Exchange Rates and International Money Transfers"))

    # Delete the default amount and type 100
    page.locator("label").filter(has_text="Amount").press("Backspace")
    page.locator("label").filter(has_text="Amount").press_sequentially('100')

    # Specify the source currency
    page.locator("#midmarketFromCurrency").get_by_role("combobox", name="Type to search...").fill("Brazilian")
    page.locator("#midmarketFromCurrency-option-1").is_hidden
    page.locator("#midmarketFromCurrency-option-0").get_by_text("BRL Brazilian Real").press("Enter")

    # Specify the destination currency
    page.locator("#midmarketToCurrency").get_by_role("combobox", name="Type to search...").fill("euro member countries")
    page.locator("#midmarketToCurrency-option-1").is_hidden
    page.locator("#midmarketToCurrency-option-0").get_by_text("EUR Euro").press("Enter")
    
    # Click convert button
    page.get_by_role("Button").get_by_text("Convert").click()
    page.get_by_role("Button").get_by_text("Convert").is_hidden

    # Assert conversion result texts
    locator = page.get_by_test_id("conversion").get_by_text(re.compile("Brazilian Reais"))
    expect(locator).to_have_text('100.00 Brazilian Reais =')

    locator = page.get_by_test_id("conversion").locator("p").nth(1)
    expect(locator).to_have_text(re.compile("^[0-9]{2}.[0-9]{5,6} Euros$"))

    locator = page.get_by_test_id("conversion").locator("p").nth(2)
    expect(locator).to_have_text(re.compile("^1 BRL = 0.[0-9]{5,6} EUR$$"))

    locator = page.get_by_test_id("conversion").locator("p").nth(3)
    expect(locator).to_have_text(re.compile("^1 EUR = [0-9]{1}.[0-9]{5,6} BRL$"))

def test_get_started_link(chromium_browser):
    page = chromium_browser
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()