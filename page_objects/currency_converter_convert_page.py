from playwright.sync_api import expect
import re


class converPage(object):
    def __init__(self, page, url) -> None:
        self.page = page
        self.page.goto(url)

        self.amount_text_box = page.locator("#amount")
        expect(self.amount_text_box).to_be_visible()
        self.from_curr_combobox = page.locator("#midmarketFromCurrency").get_by_role("combobox", name="Type to search...")
        expect(self.from_curr_combobox).to_be_visible()
        self.to_curr_combobox = page.locator("#midmarketToCurrency").get_by_role("combobox", name="Type to search...")
        expect(self.to_curr_combobox).to_be_visible()
        self.convert_btn = page.get_by_role("Button").get_by_text("Convert")
        expect(self.convert_btn).to_be_visible()
        self.charts_tab = page.locator('div > a[href="/currencycharts/"]')
        expect(self.charts_tab).to_be_visible()

        self.view_chart_btn = self.page.get_by_role("button").get_by_text("View chart")
        self.track_curr_btn = self.page.get_by_role("button").get_by_text("Track currency")
        self.view_trnsf_quote_btn = self.page.locator('a[href="/send-money/"]').get_by_text("View transfer quote")
        self.chart_headind1 = self.page.get_by_test_id('chart-container').get_by_role('heading').nth(0)
        self.chart_headind2 = self.page.get_by_test_id('chart-container').get_by_role('heading').nth(1)
        self.chart_heading2_year = self.page.locator('div[data-testid="chart-container"] div[style*="margin"] div p')

        self.chart_granularity_1Y = self.page.get_by_test_id('chart-container').get_by_role('button').get_by_text("1Y")
        self.chart_granularity_2Y = self.page.get_by_test_id('chart-container').get_by_role('button').get_by_text("2Y")


    def select_from_currency_brz(self):
        self._select_from_currency('Brazilian', 'BRL Brazilian Real')
    
    def select_to_currency_euro(self):
        self._select_to_currency('euro member countries', 'EUR Euro')

    def enter_amount(self, amount):
        self.amount_text_box.press("Backspace")
        expect(self.page.locator('div[aria-live="assertive"][class*="top-1"]')).to_be_visible
        self.amount_text_box.press_sequentially(amount)
        self.amount_text_box.press("Enter")

    def _select_from_currency(self, currency_name, expected_value):
        self.from_curr_combobox.fill(currency_name)
        self.page.locator("#midmarketFromCurrency-option-1").is_hidden
        self.page.locator("#midmarketFromCurrency-option-0").get_by_text(expected_value).press("Enter")

    def _select_to_currency(self, currency_name, expected_value):
        self.to_curr_combobox.fill(currency_name)
        self.page.locator("#midmarketToCurrency-option-1").is_hidden
        self.page.locator("#midmarketToCurrency-option-0").get_by_text(expected_value).press("Enter")

    def accept_cookie(self):
        self.page.get_by_role("button").get_by_text("Accept").click()
