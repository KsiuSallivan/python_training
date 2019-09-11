# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create_button()
        app.contact.data_contact(Contact(firstname="Kseniya", lastname="Kurashova", nickname="KsiuSallivan", email="ksiu.sallivan@gmail.com"))
        app.contact.submit_button()
        app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.select_first_contact()
    app.contact.delete_button()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts