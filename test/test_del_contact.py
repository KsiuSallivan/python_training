# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_delete_first_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create_button()
        app.contact.data_contact(Contact(firstname="Kseniya", lastname="Kurashova", nickname="KsiuSallivan", email="ksiu.sallivan@gmail.com"))
        app.contact.submit_button()
        app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.select_contact_by_index(index)
    app.contact.delete_button()
    app.contact.contact_cache_none()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
