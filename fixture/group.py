from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and  len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

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

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_group(self):
        self.select_group_by_index(0)

    def data_group(self, group):
        self.type("group_name", group.name)
        self.type("group_header", group.header)
        self.type("group_footer", group.footer)

    def create_group(self, group):
        self.open_group_page()
        self.create_button()
        self.data_group(group)
        self.submit_button()
        self.return_to_group_page()
        self.group_cache = None

    def delete_group_by_index(self, index):
        self.open_group_page()
        self.select_group_by_index(index)
        self.delete_button()
        self.return_to_group_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        self.open_group_page()
        self.select_group_by_index(index)
        self.edit_button()
        self.data_group(new_group_data)
        self.update_button()
        self.return_to_group_page()
        self.group_cache = None

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
