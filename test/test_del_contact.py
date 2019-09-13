# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Kseniya", lastname="Kurashova", nickname="KsiuSallivan",
                                            email="ksiu.sallivan@gmail.com"))
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts