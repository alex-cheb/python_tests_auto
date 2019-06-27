from objects import LocateElements as le
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AboutPage(le):
    def __init__(self):
        self.url = self.ff.current_url
    def go_to_about(self):
        self.ff.get("https://anotepad.com/about")

class FeaturesPage(le):
    def go_to_features(self):
        self.ff.get("https://anotepad.com/features")

class SettingsPage(le):
    def go_to_settings(self):
        self.ff.get("https://anotepad.com/settings")

class HomePage(le):
    def go_home(self):
        self.ff.get("https://anotepad.com")



class LoginPage(le):
    def go_to_login(self):
        print("Move to login page")
        self.ff.get("https://anotepad.com/create_account")
    def login(self, email, pwd):
        self.go_to_login()
        #elem = WebDriverWait(self.ff, 10).until(EC.presence_of_all_elements_located(le.login_email_input))
        self.ff.find_element(*self.login_email_input).clear()
        self.ff.find_element(*self.login_email_input).send_keys(email)
        self.ff.find_elements(*self.pwd_input)[1].clear()
        self.ff.find_elements(*self.pwd_input)[1].send_keys(pwd)
        self.ff.find_elements(*self.submit_button)[1].click()

    def create_acc(self, email, pwd):
        self.go_to_login()
        self.ff.find_element(*self.create_email_input).clear()
        self.ff.find_element(*self.lcreate_email_input).send_keys(email)
        self.ff.find_elements(*self.pwd_input)[0].clear()
        self.ff.find_elements(*self.pwd_input)[0].send_keys(pwd)
        self.find_elements(*self.submit_button)[0].click()

    def logout(self):
        self.ff.find_element(*self.header_logout).click()
