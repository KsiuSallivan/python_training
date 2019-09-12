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

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

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
        wd = self.app.wd
        self.type("firstname", contact.firstname)
        self.type("lastname", contact.lastname)
        self.type("nickname", contact.nickname)
        self.type("email", contact.email)

    def modify_contact(self, new_contact_data):
        self.data_contact(new_contact_data)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//input[@name='selected[]']"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                firstname = element.find_element_by_xpath("//td[3]")
                lastname = element.find_element_by_xpath("//td[2]")
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname))
        return list(self.contact_cache)

    def contact_cache_none(self):
        self.contact_cache = None