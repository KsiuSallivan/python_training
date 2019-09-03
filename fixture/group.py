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
        self.type("group_name", group.name)
        self.type("group_header", group.header)
        self.type("group_footer", group.footer)

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_group(self, new_group_data):
        self.data_group(new_group_data)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))