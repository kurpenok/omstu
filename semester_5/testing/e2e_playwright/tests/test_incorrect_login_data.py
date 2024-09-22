from pages.login_po import LoginPage


def test_login_with_invalid_credentials(page):
    login_page = LoginPage(page)
    login_page.open()

    login_page.input_username("standard_user")
    login_page.input_password("wrong_password")
    login_page.click_login()

    error_message = login_page.get_error_message()
    assert (
        error_message
        == "Epic sadface: Username and password do not match any user in this service"
    )
