from selenium import webdriver
from selenium.webdriver.common.by import By

#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager



class LocateElements(object):
    ff: WebDriver

    def __init__(self):
        # ch = webdriver.Chrome(ChromeDriverManager().install())

        self.ff = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("Starting browser")

    def open_home_page(self):
        print("Go to home page")
        self.ff.get("https://anotepad.com")
        self.ff.maximize_window()

    def close_window(self):
        print("Quit")
        self.ff.quit()

    def open_login_page(self):
        self.ff.get("https://anotepad.com/create_account")

    def open_settings_page(self):
        self.ff.get("https://anotepad.com/settings")

    def element_visibility(self, element):
        return self.ff.find_element(element).is_displayed()



     # Elements locators

    header_logo = (By.CSS_SELECTOR, "#logo_img")
    header_motto = (By.CSS_SELECTOR, "#subTitle")
    header_home = (By.PARTIAL_LINK_TEXT, 'Home')
    header_features = (By.PARTIAL_LINK_TEXT, 'Features')
    heder_about = (By.PARTIAL_LINK_TEXT, 'About')
    header_settings = (By.PARTIAL_LINK_TEXT, 'Settings')
    header_login = (By.PARTIAL_LINK_TEXT, 'Login/Register')
    header_logout = (By.PARTIAL_LINK_TEXT, 'Logout')

    #home page
    note_title = (By.CSS_SELECTOR, '#edit_title')
    note_content = (By.CSS_SELECTOR, '#edit_textarea')
    save_button = (By.CSS_SELECTOR, '#btnSaveNote')
    public_note_button = (By.CSS_SELECTOR, "#noteAccessLabel")
    enable_richtext_button = (By.CSS_SELECTOR, "#btnEnableRichText")
    share_button = (By.CSS_SELECTOR, ".atc_s.addthis_button_compact")
    notes_block = (By.CSS_SELECTOR, "div.notes")
    sort_by_title_button = (By.XPATH, "//a[@ title = 'Sorted Alphabetically']")
    sort_by_date_button = (By.XPATH, "//a[@title = 'Most Recent First']")
    folders_list = (By.CSS_SELECTOR, "#folder-list")
    manage_folders_button = (By.PARTIAL_LINK_TEXT, "Manage Folders")
    note_list = (By.CSS_SELECTOR, "ul#savedNotes")

    #register/login page
    create_email_input = (By.CSS_SELECTOR, "input#registerEmail")
    login_email_input = (By.CSS_SELECTOR, "#loginEmail")
    pwd_input = (By.CSS_SELECTOR, "#password")
    #login_pwd_input = (By.CSS_SELECTOR, "#password")
    forgot_password = (By.XPATH, "//a[@href = 'forgot']")
    submit_button = (By.CSS_SELECTOR, "#submit")



