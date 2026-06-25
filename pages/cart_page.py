class CartPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator('[data-test="title"]')
        self.inventory_name = page.locator('[data-test="inventory-item-name"]')
        self.inventory_description = page.locator('[data-test="inventory-item-desc"]')
        self.item_quantity = page.locator('[data-test="item-quantity"]')
        self.price = page.locator('[data-test="inventory-item-price"]')
        self.remove_button = page.locator('[data-test="remove-sauce-labs-backpack"]')
        self.continue_shopping_button = page.locator('[data-test="continue-shopping"]')
        self.checkout_button = page.locator('[data-test="checkout"]')

    def go_to_checkout(self):
        self.checkout_button.click()

    def go_to_continue_shopping(self):
        self.continue_shopping_button.click()