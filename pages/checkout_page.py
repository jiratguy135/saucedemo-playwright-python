class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator('[data-test="title"]')
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.continue_shopping_button = page.locator('[data-test="continue-shopping"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')



    def go_to_checkout(self):
        self.checkout_button.click()

    def go_to_continue_shopping(self):
        self.continue_shopping.click()

    


