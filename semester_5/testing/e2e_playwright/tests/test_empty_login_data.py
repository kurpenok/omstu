from pages.login_po import LoginPage


def test_login_with_invalid_credentials(page):
    login_page = LoginPage(page)
    login_page.open()

    login_page.click_login()

    error_message = login_page.get_error_message()
    assert error_message == "Epic sadface: Username is required"
