import pytest, allure
from objects import LocateElements as le
from pages import LoginPage


page = LoginPage()

#@pytest.fixture(scope='session')
# @pytest.fixture
def base_actions():

    page.go_to_login()
    yield
    page.logout()
    page.close_window()


#@allure.step("Login Positive Test")

def test_valid_data(base_actions):
    email = "2@e.ee"
    pwd = "2"
    page.login(email, pwd)
    print(le.header_settings)
    print(type(le.header_settings))
    print(page)
    assert page.element_visibility(le.header_settings), 'Not logged in'


test_valid_data(base_actions())