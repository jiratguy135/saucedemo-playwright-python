from pages.cart_page import CartPage
from playwright.sync_api import expect


def test_added_product_appears_in_cart(page, inventory_page):
    inventory_page.add_backpack_to_cart()
    expect(inventory_page.cart_badge).to_have_text("1")
    inventory_page.go_to_cart()

    cart_page = CartPage(page)
    expect(page).to_have_url("/cart.html")
    expect(cart_page.inventory_name).to_have_text("Sauce Labs Backpack")
    expect(cart_page.item_quantity).to_have_text("1")
    expect(cart_page.price).to_have_text("$29.99")