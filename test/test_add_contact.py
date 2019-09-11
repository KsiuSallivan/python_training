# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Kseniya", lastname="Kurashova", nickname="KsiuSallivan", email="ksiu.sallivan@gmail.com")
    app.open_home_page()
    app.contact.create_button()
    app.contact.data_contact(contact)
    app.contact.submit_button()
    app.contact.contact_cache_none()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
