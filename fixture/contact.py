from model.contact import Contact


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
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

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

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def data_contact(self, contact):
        self.type("firstname", contact.firstname)
        self.type("lastname", contact.lastname)
        self.type("nickname", contact.nickname)
        self.type("email", contact.email)

    def create_contact(self, contact):
         self.app.open_home_page()
         self.create_button()
         self.data_contact(contact)
         self.submit_button()
         self.app.open_home_page()

    def delete_first_contact(self):
        self.app.open_home_page()
        self.select_first_contact()
        self.delete_button()
        self.app.open_home_page()

    def modify_first_contact(self, new_contact_data):
        self.app.open_home_page()
        self.select_first_contact()
        self.edit_button()
        self.data_contact(new_contact_data)
        self.update_button()
        self.app.open_home_page()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_xpath("//input[@name='selected[]']"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            id = element.find_element_by_tag_name("input").get_attribute("value")
            firstname = element.find_element_by_xpath(".//td[3]").text
            lastname = element.find_element_by_xpath(".//td[2]").text
            contacts.append(Contact(id=id, firstname=firstname, lastname=lastname))
        return contacts