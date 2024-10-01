from playwright.sync_api import Page


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.products_sort_selector = page.locator(
            "select[class='product_sort_container']"
        )
        self.inventories_prices = page.locator("div[class='inventory_item_price']")

    def sort_products(self):
        self.products_sort_selector.select_option("lohi")

    def get_products_prices(self):
        prices_elements = self.inventories_prices.all_inner_texts()
        prices = [float(price[1:]) for price in prices_elements]
        return prices
