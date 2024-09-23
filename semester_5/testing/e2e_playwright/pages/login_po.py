from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.page.goto("https://www.saucedemo.com/")
        self.username = page.locator("input[name='user-name']")
        self.password = page.locator("input[name='password']")
        self.login_button = page.locator("input[name='login-button']")
        self.login_error = page.locator("h3[data-test='error']")

    def login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
