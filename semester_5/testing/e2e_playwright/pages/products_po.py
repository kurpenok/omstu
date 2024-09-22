from playwright.sync_api import Page


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_sort_selector = "select[data-test='product-sort-container']"
        self.inventories_prices = "div[class='inventory_item_price']"

    def sort_products(self):
        self.page.select_option(self.product_sort_selector, "lohi")

    def get_products_prices(self):
        expression = "prices => prices.map(price => price.innerText)"
        prices_elements = self.page.eval_on_selector_all(
            self.inventories_prices, expression
        )
        prices = [float(price[1:]) for price in prices_elements]
        return prices
