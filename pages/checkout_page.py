class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator('[data-test="title"]')
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.continue_shopping_button = page.locator('[data-test="continue-shopping"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')

        self.firstname_field = page.locator('[data-test="firstName"]')
        self.lastname_field = page.locator('[data-test="lastName"]')
        self.postalcode_field = page.locator('[data-test="postalCode"]')
        self.error_message = page.locator('[data-test="error"]')
        self.cancel_button = page.locator('[data-test="cancel"]')

        self.complete_header = page.locator('[data-test="complete-header"]')
        self.complete_text = page.locator('[data-test="complete-text"]')
        self.back_home_button = page.locator('[data-test="back-to-products"]')


    def go_to_checkout(self):
        self.checkout_button.click()

    def go_to_continue_shopping(self):
        self.continue_shopping_button.click()

    def click_continue(self):
        self.continue_button.click()

    def click_finish(self):
        self.finish_button.click()

    def information(self,firstname,lastname,postalcode):
        self.firstname_field.fill(firstname)
        self.lastname_field.fill(lastname)
        self.postalcode_field.fill(postalcode)
    


