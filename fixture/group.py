from selenium.webdriver.common.by import By
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups(self):
        wd = self.app.driver
        wd.find_element(By.LINK_TEXT, "group page").click()

    def open_groups_page(self):
        wd = self.app.driver
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new")) > 0):
            wd.find_element(By.LINK_TEXT, "groups").click()

    def count(self):
        wd = self.app.driver
        self.open_groups_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

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

    def create(self, group):
        wd = self.app.driver
        self.open_groups_page()
        # create new group
        wd.find_element(By.NAME, "new").click()
        self.fill_form(group)
        # submit
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups()
        self.group_cache = None

    def edit_first(self, group):
        self.edit_group_by_index(0, group)

    def edit_group_by_index(self, index, group):
        wd = self.app.driver
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element(By.NAME, "edit").click()
        self.fill_form(group)
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups()
        self.group_cache = None

    def edit_group_by_id(self, id, group):
        wd = self.app.driver
        self.open_groups_page()
        self.select_group_by_id(id)
        wd.find_element(By.NAME, "edit").click()
        self.fill_form(group)
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups()
        self.group_cache = None

    def delete_first(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.driver
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.driver
        self.open_groups_page()
        self.select_group_by_id(id)
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.driver
        wd.find_element(By.NAME, "selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.driver
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.driver
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.driver
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                group_id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=group_id))
        return list(self.group_cache)
