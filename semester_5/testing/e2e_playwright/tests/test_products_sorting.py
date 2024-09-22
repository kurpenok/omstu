from pages.login_po import LoginPage
from pages.products_po import ProductsPage


def test_sort_products_low_to_high(page):
    login_page = LoginPage(page)
    login_page.open()

    login_page.input_username("standard_user")
    login_page.input_password("secret_sauce")
    login_page.click_login()

    products_page = ProductsPage(page)
    products_page.sort_products()

    prices = products_page.get_products_prices()
    assert prices == sorted(prices)
