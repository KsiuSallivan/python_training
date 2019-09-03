class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_button(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def submit_button(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def edit_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt='Edit']").click()

    def update_button(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='selected[]']").click()

    def delete_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def data_contact(self, contact):
        wd = self.app.wd
        self.type("contact_firstname", contact.firstname)
        self.type("contact_lastname", contact.lastname)
        self.type("contact_nickname", contact.nickname)
        self.type("contact_email", contact.email)

    def modify_first_contact(self, new_contact_data):
        self.data_contact(new_contact_data)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//input[@name='selected[]']"))
