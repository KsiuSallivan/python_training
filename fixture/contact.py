from model.contact import Contact
from model.group import Group
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_button(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def submit_button(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def update_button(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def select_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id and "img[alt='Edit']").click()

    def select_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

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
        self.type("address", contact.address)
        self.type("email", contact.email)
        self.type("email2", contact.email2)
        self.type("email3", contact.email3)
        self.type("home", contact.homephone)
        self.type("mobile", contact.mobilephone)
        self.type("work", contact.workphone)
        self.type("phone2", contact.secondaryphone)

    def create_contact(self, contact):
        self.app.open_home_page()
        self.create_button()
        self.data_contact(contact)
        self.submit_button()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        self.delete_button()
        wd.find_element_by_css_selector("div.msgbox")
        self.app.open_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_id(0)

    def modify_contact_by_id(self, id, new_contact_data):
        self.app.open_home_page()
        self.select_contact_to_edit_by_id(id)
        self.data_contact(new_contact_data)
        self.update_button()
        self.app.open_home_page()
        self.contact_cache = None

    def modify_contact_by_index(self, index, new_contact_data):
        self.app.open_home_page()
        self.select_contact_to_edit_by_index(index)
        self.data_contact(new_contact_data)
        self.update_button()
        self.app.open_home_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_id(0)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_xpath("//input[@name='selected[]']"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, workphone=workphone, mobilephone=mobilephone,
                       secondaryphone=secondaryphone, address=address,
                       email=email, email2=email2, email3=email3)

    def add_contact_to_group(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_css_selector("option[value='%s']" % id).click()
        wd.find_element_by_name("add").click()
        self.app.open_home_page()
        wd.find_element_by_name("group").click()
        wd.find_element_by_css_selector("option[value]").click()

    def del_contact_from_group(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("group").click()
        wd.find_element_by_css_selector("option[value='%s']" % id).click()
        self.select_contact_by_id(id)
        wd.find_element_by_css_selector("input[name='remove']").click()
        self.app.open_home_page()
        wd.find_element_by_name("group").click()
        wd.find_element_by_css_selector("option[value]").click()


    # def get_contact_info_from_view_page(self, index):
    #     wd = self.app.wd
    #     self.select_contact_to_view_by_index(index)
    #     text = wd.find_element_by_id("content").text
    #     homephone = re.search("H: (.*)", text).group(1)
    #     workphone = re.search("W: (.*)", text).group(1)
    #     mobilephone = re.search("M: (.*)", text).group(1)
    #     secondaryphone = re.search("P: (.*)", text).group(1)
    #     return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone,
    #                    secondaryphone=secondaryphone)
