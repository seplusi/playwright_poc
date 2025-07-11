from playwright.sync_api import expect
from page_objects.currency_converter_home_page import convertHomePage
import re


class convertPage(convertHomePage):
    def __init__(self, page, url, timeout=None) -> None:
        super().__init__(page, url, timeout)

        self.popup_elements = self.page.locator("yld-tag-host-campaign")
        self.convert_result_parent_ele = self.page.locator('div[data-testid="conversion"][class*="grid"]')


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
