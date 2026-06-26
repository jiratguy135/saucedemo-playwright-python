class CheckoutCompletePage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator('[data-test="title"]')
        self.complete_header = page.locator('[data-test="complete-header"]')
        self.complete_text = page.locator('[data-test="complete-text"]')
        self.back_home_button = page.locator('[data-test="back-to-products"]')

    def click_back_home(self):
        self.back_home_button.click()
