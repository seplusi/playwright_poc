import re
from playwright.sync_api import Page, expect

def test_home_page(page: Page):
    page.goto("https://www.xe.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Currency Exchange Rates and International Money Transfers"))

    page.locator("label").filter(has_text="Amount").press("Backspace")
    page.locator("label").filter(has_text="Amount").press_sequentially('100')

    page.locator("#midmarketFromCurrency").get_by_role("combobox", name="Type to search...").fill("Brazilian")
    page.locator("#midmarketFromCurrency-option-1").is_hidden
    page.locator("#midmarketFromCurrency-option-0").get_by_text("BRL Brazilian Real").press("Enter")
    #page.locator("#midmarketFromCurrency").press("Enter")

    page.locator("#midmarketToCurrency").get_by_role("combobox", name="Type to search...").fill("euro member countries")
    page.locator("#midmarketToCurrency-option-1").is_hidden
    page.locator("#midmarketToCurrency-option-0").get_by_text("EUR Euro").press("Enter")
    
    page.get_by_role("Button").get_by_text("Convert").click()
    page.get_by_role("Button").get_by_text("Convert").is_hidden

    locator = page.get_by_test_id("conversion").get_by_text(re.compile("Brazilian Reais"))
    expect(locator).to_have_text('100.00 Brazilian Reais =')

    locator = page.get_by_test_id("conversion").locator("p").nth(1)
    expect(locator).to_have_text(re.compile("^[0-9]{2}.[0-9]{6} Euros$"))

    locator = page.get_by_test_id("conversion").locator("p").nth(2)
    expect(locator).to_have_text(re.compile("^1 BRL = 0.[0-9]{6} EUR$$"))

    locator = page.get_by_test_id("conversion").locator("p").nth(3)
    expect(locator).to_have_text(re.compile("^1 EUR = [0-9]{1}.[0-9]{5} BRL$"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()