from selenium import webdriver
from fixture.session_contact import SessionHelperContact
from fixture.contact import ContactHelper


class ApplicationContact:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1070, 760)
        self.session = SessionHelperContact(self)
        self.contact = ContactHelper(self)

    def destroy(self):
        self.driver.quit()

    def go_to_home_page(self):
        self.driver.get("http://localhost/addressbook/")
