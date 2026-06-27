class CheckoutOverviewPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator('[data-test="title"]')

        self.item_name = page.locator('[data-test="inventory-item-name"]')
        self.item_price = page.locator('[data-test="inventory-item-price"]')

        self.total_price_label = page.locator('[data-test="subtotal-label"]')
        self.tax_label = page.locator('[data-test="tax-label"]')
        self.total_price_tax_label = page.locator('[data-test="total-label"]')

        self.cancel_button = page.locator('[data-test="cancel"]')
        self.finish_button = page.locator('[data-test="finish"]')
        

    def click_finish(self):
        self.finish_button.click()

    def click_cancel(self):
        self.cancel_button.click()

    def sum_total(self):
        total_price = float(self.total_price_label.inner_text().split("$")[1])
        tax = float(self.tax_label.inner_text().split("$")[1])
        return round(total_price + tax, 2)