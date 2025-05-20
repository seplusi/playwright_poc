class converPage(object):
    def __init__(self, page) -> None:
        self.page = page

        self.amount_text_box = page.locator("#amount")
        self.from_curr_combobox = page.locator("#midmarketFromCurrency").get_by_role("combobox", name="Type to search...")
        self.to_curr_combobox = page.locator("#midmarketToCurrency").get_by_role("combobox", name="Type to search...")
        self.convert_btn = page.get_by_role("Button").get_by_text("Convert")

    def navigate(self, url):
        self.page.goto(url)

    def select_from_currency_brz(self):
        self._select_from_currency('Brazilian', 'BRL Brazilian Real')
    
    def select_to_currency_euro(self):
        self._select_to_currency('euro member countries', 'EUR Euro')

    def enter_amount(self, amount):
        self.amount_text_box.press("Backspace")
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
