from playwright.sync_api import Page, expect

from pages.login_po import LoginPage


def test_login_with_empty_data(page: Page):
    login_page = LoginPage(page)
    login_page.login("", "")
    expect(login_page.login_error).to_have_text("Epic sadface: Username is required")
