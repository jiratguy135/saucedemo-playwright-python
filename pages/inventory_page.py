class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator('[data-test="title"]')
        self.inventory_item_name = page.locator('[data-test="inventory-item-name"]')
        self.add_backpack_to_cart_button = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.remove_backpack_from_cart_button = page.locator('[data-test="remove-sauce-labs-backpack"]')
        self.cart_button = page.locator('[data-test="shopping-cart-link"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')


    def add_backpack_to_cart(self):
        self.add_backpack_to_cart_button.click()

    def remove_backpack_from_cart(self):
        self.remove_backpack_from_cart_button.click()

    def go_to_cart(self):
        self.cart_button.click()
