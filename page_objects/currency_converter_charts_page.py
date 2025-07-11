from playwright.sync_api import expect
from page_objects.currency_converter_home_page import convertHomePage
import re


class chartsPage(convertHomePage):
    def __init__(self, page, url, timeout=None) -> None:
        super().__init__(page, url, timeout)

        self.view_chart_btn = self.page.get_by_role("button").get_by_text("View chart")
        self.track_curr_btn = self.page.get_by_role("button").get_by_text("Track currency")
        self.view_trnsf_quote_btn = self.page.locator('a[href="/send-money/"]').get_by_text("View transfer quote")
        self.chart_headind1 = self.page.get_by_test_id('chart-container').get_by_role('heading').nth(0)
        self.chart_headind2 = self.page.get_by_test_id('chart-container').get_by_role('heading').nth(1)
        self.chart_heading2_year = self.page.locator('div[data-testid="chart-container"] div[style*="margin"] div p')

        self.chart_granularity_1Y = self.page.get_by_test_id('chart-container').get_by_role('button').get_by_text("1Y")
        self.chart_granularity_2Y = self.page.get_by_test_id('chart-container').get_by_role('button').get_by_text("2Y")

        self.popup_elements = self.page.locator("yld-tag-host-campaign")


    def select_from_currency_brz(self):
        self._select_from_currency('Brazilian', 'BRL Brazilian Real')
    
    def select_to_currency_euro(self):
        self._select_to_currency('euro member countries', 'EUR Euro')

    def enter_amount(self, amount):
        self.amount_text_box.press("Backspace")
        expect(self.page.locator('div[aria-live="assertive"][class*="top-1"]')).to_be_visible()
        self.amount_text_box.press_sequentially(amount)
        expect(self.amount_text_box).to_have_value(f"{amount}")
        self.amount_text_box.press("Enter")
