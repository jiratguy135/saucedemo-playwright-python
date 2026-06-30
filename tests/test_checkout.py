from pages.cart_page import CartPage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
import pytest
from playwright.sync_api import expect

def test_checkout_single_item_completes_successfully(page, inventory_page):
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(page)
    expect(cart_page.inventory_name).to_have_text('Sauce Labs Backpack')
    expect(cart_page.price).to_have_text('$29.99')
    cart_page.go_to_checkout()

    checkout_information_page = CheckoutInformationPage(page)
    checkout_information_page.fill_information("John","Doe","12345")
    checkout_information_page.click_continue()

    checkout_overview_page = CheckoutOverviewPage(page)
    expect(checkout_overview_page.item_name).to_have_text('Sauce Labs Backpack')
    expect(checkout_overview_page.item_price).to_have_text('$29.99')
    expect(checkout_overview_page.total_price_tax_label).to_have_text(f'Total: ${checkout_overview_page.sum_total():.2f}')
    checkout_overview_page.click_finish()

    checkout_complete_page = CheckoutCompletePage(page)
    expect(checkout_complete_page.complete_header).to_have_text('Thank you for your order!')
    expect(page).to_have_url("/checkout-complete.html")

def test_checkout_without_first_name_shows_error(page, inventory_page):
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(page)
    cart_page.go_to_checkout()

    checkout_information_page = CheckoutInformationPage(page)
    checkout_information_page.click_continue()
    expect(checkout_information_page.information_error).to_have_text('Error: First Name is required')

@pytest.mark.xfail(reason="BUG-001: ระบบยอมให้ checkout cart ว่างได้ (ควรถูกบล็อก)")
def test_checkout_with_empty_cart_should_be_blocked(page, inventory_page):
    inventory_page.go_to_cart()

    cart_page = CartPage(page)
    cart_page.go_to_checkout()

    checkout_information_page = CheckoutInformationPage(page)
    checkout_information_page.fill_information("John","Doe","12345")
    checkout_information_page.click_continue()

    checkout_overview_page = CheckoutOverviewPage(page)
    expect(checkout_overview_page.total_price_tax_label).to_have_text(f'Total: ${checkout_overview_page.sum_total():.2f}')
    page.screenshot(path="bugs/evidence/bug-001-overview.png")
    checkout_overview_page.click_finish()

    checkout_complete_page = CheckoutCompletePage(page)
    page.screenshot(path="bugs/evidence/bug-001-complete.png")
    expect(page).not_to_have_url("/checkout-complete.html")
    