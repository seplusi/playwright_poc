from playwright.sync_api import expect


class convertHomePage(object):
    def __init__(self, page, url, timeout=None) -> None:
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

    def accept_cookie(self):
        # No need to wait because click action already waits for the iimplicit wait
        self.page.get_by_role("button").get_by_text("Accept").click()

    def dismiss_popup(self, timeout=30000):
        # We never know when the popup is going to show up. Wait for a long time
        expect(self.popup_elements).to_have_count(count=5, timeout=timeout)
        self.page.keyboard.press("Escape")

    def _select_from_currency(self, currency_name, expected_value):
        self.from_curr_combobox.fill(currency_name)
        expect(self.page.locator("#midmarketFromCurrency-option-1")).to_be_hidden()
        self.page.locator("#midmarketFromCurrency-option-0").get_by_text(expected_value).press("Enter")

    def _select_to_currency(self, currency_name, expected_value):
        self.to_curr_combobox.fill(currency_name)
        expect(self.page.locator("#midmarketToCurrency-option-1")).to_be_hidden()
        self.page.locator("#midmarketToCurrency-option-0").get_by_text(expected_value).press("Enter")
