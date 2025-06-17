import re
from playwright.sync_api import expect
from page_objects.mobile_currency_converter_convert_page import mobileConverPage

#work in progress
def test_currency_converter_page_chrome(galaxy_s8_browser):
    page = mobileConverPage(galaxy_s8_browser)
    
    # Accept cookie
    page.accept_cookie()

    # Expect a title "to contain" a substring.
    expect(page.page).to_have_title(re.compile("Currency Exchange Rates and International Money Transfers"))

    # Delete the default amount and type 100
    page.enter_amount("100")

    # Specify the source currency
    #page.select_from_currency_brz()

    # Specify the destination currency
    #page.select_to_currency_euro()
    
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

