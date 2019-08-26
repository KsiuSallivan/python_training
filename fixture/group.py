class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create_button(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def submit_button(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def edit_button(self):
        wd = self.app.wd
        wd.find_element_by_name("edit").click()

    def update_button(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def delete_button(self):
        wd = self.app.wd
        wd.find_element_by_name("delete").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def data_group(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

