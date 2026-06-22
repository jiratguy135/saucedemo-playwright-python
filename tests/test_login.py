from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect


def test_valid_login_redirects_to_inventory(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user","secret_sauce")

    inventory_page = InventoryPage(page)
    expect(inventory_page.title).to_contain_text("Products")
    expect(page).to_have_url("/inventory.html")