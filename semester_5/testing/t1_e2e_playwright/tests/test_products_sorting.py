from playwright.sync_api import Page

from pages.login_po import LoginPage
from pages.products_po import ProductsPage


def test_products_sorting(page: Page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(page)
    products_page.sort_products()

    prices = products_page.get_products_prices()
    assert prices == sorted(prices)
