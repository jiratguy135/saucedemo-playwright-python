from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from playwright.sync_api import expect

def test_function_checkout(page):
    login_page1 = CheckoutInformationPage(page)
    login_page2 = CheckoutOverviewPage(page)
    login_page3 = CheckoutCompletePage(page)

def test_valid_login_redirects_to_inventory(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user","secret_sauce")

    inventory_page = InventoryPage(page)
    expect(inventory_page.title).to_contain_text("Products")
    expect(page).to_have_url("/inventory.html")

def test_locked_out_user_shows_error(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("locked_out_user","secret_sauce")
    
    expect(login_page.error_message).to_contain_text("Epic sadface: Sorry, this user has been locked out.")
    expect(page).to_have_url("/")
    
def test_login_with_invalid_password_shows_error(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user","test")
    
    expect(login_page.error_message).to_contain_text("Epic sadface: Username and password do not match any user in this service")
    expect(page).to_have_url("/")

def test_login_with_invalid_username_shows_error(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("test","secret_sauce")
    
    expect(login_page.error_message).to_contain_text("Epic sadface: Username and password do not match any user in this service")
    expect(page).to_have_url("/")

def test_login_with_empty_username_shows_required_error(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("","secret_sauce")
    
    expect(login_page.error_message).to_contain_text("Epic sadface: Username is required")
    expect(page).to_have_url("/")

def test_login_with_empty_password_shows_required_error(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user","")
    
    expect(login_page.error_message).to_contain_text("Epic sadface: Password is required")
    expect(page).to_have_url("/")

def test_login_with_empty_credentials_shows_error(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("","")
    
    expect(login_page.error_message).to_contain_text("Epic sadface: Username is required")
    expect(page).to_have_url("/")