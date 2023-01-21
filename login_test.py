import pytest
import allure
import literals
from objects import LocateElements as le
from pages import LoginPage


page = LoginPage()

#@pytest.fixture(scope='session')
#@pytest.fixture
def base_actions():

    page.go_to_login()
    yield
    page.logout()
    page.close_window()


#@allure.step("Login with valid credentials")
def test_valid_credentials_login(base_actions) -> None:
    """Verify that the when the user with valid credentials
    logs in, the settings menu becomes visible"""    
    page.login(literals.email, literals.pwd)
    assert page.element_visibility(le.header_settings), 'Not logged in'

