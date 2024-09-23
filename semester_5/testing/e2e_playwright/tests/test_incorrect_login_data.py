from playwright.sync_api import Page, expect

from pages.login_po import LoginPage


def test_login_with_wrong_password(page: Page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "wrong_password")
    expect(login_page.login_error).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )
