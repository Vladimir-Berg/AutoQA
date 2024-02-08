from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups(self):
        wd = self.app.driver
        wd.find_element(By.LINK_TEXT, "group page").click()

    def count(self):
        wd = self.app.driver
        self.open_groups_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def create(self, group):
        wd = self.app.driver
        self.open_groups_page()
        # create new group
        wd.find_element(By.NAME, "new").click()
        self.fill_form(group)
        # submit
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups()

    def edit(self, group):
        wd = self.app.driver
        self.open_groups_page()
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.NAME, "edit").click()
        self.fill_form(group)
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups()

    def fill_form(self, group):
        wd = self.app.driver
        self.change_form_text("group_name", group.name)
        self.change_form_text("group_header", group.header)
        self.change_form_text("group_footer", group.footer)

    def change_form_text(self, field_name, text):
        wd = self.app.driver
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def delete_first(self):
        wd = self.app.driver
        self.open_groups_page()
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups()

    def open_groups_page(self):
        wd = self.app.driver
        wd.find_element(By.LINK_TEXT, "groups").click()
