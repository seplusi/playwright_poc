import re
from playwright.sync_api import expect
from playwright.sync_api._generated import Page
from page_objects.currency_converter_convert_page import convertPage
from page_objects.currency_converter_charts_page import chartsPage

def test_currency_converter_page_chrome(chromium_browser: Page):
    page = convertPage(chromium_browser, "https://www.xe.com/")
    
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
    expect(page.convert_btn).to_be_hidden()

    # Assert conversion result texts
    expect(page.convert_result_parent_ele.get_by_text(re.compile("Brazilian Real"))).to_have_text('100.00 Brazilian Real =')
    expect(page.convert_result_parent_ele.locator("p").nth(1)).to_have_text(re.compile("^[0-9]{2}.[0-9]{4,6} Euro$"))
    expect(page.convert_result_parent_ele.locator("p").nth(2)).to_have_text(re.compile("^1 BRL = 0.[0-9]{4,6} EUR$$"))
    expect(page.convert_result_parent_ele.locator("p").nth(3)).to_have_text(re.compile("^1 EUR = [0-9]{1}.[0-9]{4,6} BRL$"))

def test_currency_converter_page_firefox(firefox_browser: Page):
    pageObj = convertPage(firefox_browser, "https://www.xe.com/")
    
    # Accept cookie
    pageObj.accept_cookie()

    # Expect a title "to contain" a substring.
    expect(pageObj.page).to_have_title(re.compile("Currency Exchange Rates and International Money Transfers"))

    # Delete the default amount and type 100
    pageObj.enter_amount("100")

    # Specify the source currency
    pageObj.select_from_currency_brz()

    # Specify the destination currency
    pageObj.select_to_currency_euro()
    
    # Click convert button
    pageObj.convert_btn.click()
    expect(pageObj.convert_btn).to_be_hidden()

    # Assert conversion result texts
    expect(pageObj.convert_result_parent_ele.get_by_text(re.compile("Brazilian Real"))).to_have_text('100.00 Brazilian Real =')
    expect(pageObj.convert_result_parent_ele.locator("p").nth(1)).to_have_text(re.compile("^[0-9]{2}.[0-9]{4,6} Euro$"))
    expect(pageObj.convert_result_parent_ele.locator("p").nth(2)).to_have_text(re.compile("^1 BRL = 0.[0-9]{4,6} EUR$$"))
    expect(pageObj.convert_result_parent_ele.locator("p").nth(3)).to_have_text(re.compile("^1 EUR = [0-9]{1}.[0-9]{4,6} BRL$"))

def test_currency_converter_charts_chrome(chromium_browser: Page):
    pageObj = chartsPage(chromium_browser, "https://www.xe.com/")
    
    # Accept cookie
    pageObj.accept_cookie()

    # Expect a title "to contain" a substring.
    expect(pageObj.page).to_have_title(re.compile("Currency Exchange Rates and International Money Transfers"))

    # Click charts tab
    pageObj.charts_tab.click()

    # Wait for view chart button
    expect(pageObj.view_chart_btn).to_be_visible()

    # Wait and dismiss popup
    pageObj.dismiss_popup()

    # Specify the source currency
    pageObj.select_from_currency_brz()

    # Specify the destination currency
    pageObj.select_to_currency_euro()
    
    # View chart button is no longer displayed
    expect(pageObj.view_chart_btn).to_be_hidden()

    # Make elements assertions
    expect(pageObj.track_curr_btn).to_be_visible()
    expect(pageObj.view_trnsf_quote_btn).to_be_visible()
    expect(pageObj.chart_headind1).to_have_text("BRL to EUR Chart")
    expect(pageObj.chart_headind2).to_have_text(re.compile("^-[0-9].[0-9]{2}%$"))
    expect(pageObj.chart_heading2_year).to_have_text('(1Y)')

    # Test granularity chart background color
    expect(pageObj.chart_granularity_1Y).to_have_css("background-color", "rgb(0, 113, 235)")
    expect(pageObj.chart_granularity_2Y).to_have_css("background-color", "rgb(255, 255, 255)")

    pageObj.chart_granularity_2Y.click()
    expect(pageObj.chart_heading2_year).to_have_text('(2Y)')
    expect(pageObj.chart_granularity_2Y).to_have_css("background-color", "rgb(0, 113, 235)")
    expect(pageObj.chart_granularity_1Y).to_have_css("background-color", "rgb(255, 255, 255)")

def test_currency_converter_charts_firefox(firefox_browser: Page):
    pageObj = chartsPage(firefox_browser, "https://www.xe.com/")
    
    # Accept cookie
    pageObj.accept_cookie()

    # Expect a title "to contain" a substring.
    expect(pageObj.page).to_have_title(re.compile("Currency Exchange Rates and International Money Transfers"))

    # Click charts tab
    pageObj.charts_tab.click()

    # Wait for view chart button
    expect(pageObj.view_chart_btn).to_be_visible(timeout=10000)

    # Wait and dismiss popup
    pageObj.dismiss_popup()

    # Specify the source currency
    pageObj.select_from_currency_brz()

    # Specify the destination currency
    pageObj.select_to_currency_euro()
    
    # View chart button is no longer displayed
    expect(pageObj.view_chart_btn).to_be_hidden()

    # Make elements assertions
    expect(pageObj.track_curr_btn).to_be_visible()
    expect(pageObj.view_trnsf_quote_btn).to_be_visible()
    expect(pageObj.chart_headind1).to_have_text("BRL to EUR Chart")
    expect(pageObj.chart_headind2).to_have_text(re.compile("^-[0-9].[0-9]{2}%$"))
    expect(pageObj.chart_heading2_year).to_have_text('(1Y)')

    # Test granularity chart background color
    expect(pageObj.chart_granularity_1Y).to_have_css("background-color", "rgb(0, 113, 235)")
    expect(pageObj.chart_granularity_2Y).to_have_css("background-color", "rgb(255, 255, 255)")

    pageObj.chart_granularity_2Y.click()
    expect(pageObj.chart_heading2_year).to_have_text('(2Y)')
    expect(pageObj.chart_granularity_2Y).to_have_css("background-color", "rgb(0, 113, 235)")
    expect(pageObj.chart_granularity_1Y).to_have_css("background-color", "rgb(255, 255, 255)")