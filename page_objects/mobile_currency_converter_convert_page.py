from playwright.sync_api import expect
from page_objects.currency_converter_convert_page import converPage


class mobileConverPage(object):
    def __init__(self, page) -> None:
        self.page = page
        self.navigate("https://www.xe.com/")

        self.amount_text_box = page.locator("span.amount-input")
        self.from_curr_combobox = page.locator("#midmarketFromCurrency").get_by_role("button")
        self.to_curr_combobox = page.locator("#midmarketToCurrency").get_by_role("combobox", name="Type to search...")
        self.convert_btn = page.get_by_role("Button").get_by_text("Convert")

    def navigate(self, url):
        self.page.goto(url)

    def enter_amount(self, amount):
        self.amount_text_box.click()
        self.amount_text_box.press("Backspace")
        self.page.locator('div[aria-live="assertive"]').get_by_text('Please enter a valid amount')
        self.amount_text_box.click()
        self.amount_text_box.press_sequentially(amount)
        self.amount_text_box.press("Enter")

    def accept_cookie(self):
        self.page.get_by_role("button").get_by_text("Accept").click()
