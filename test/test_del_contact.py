# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_button()
        app.contact.data_contact(Contact(firstname="Kseniya", lastname="Kurashova", nickname="KsiuSallivan",
                                         email="ksiu.sallivan@gmail.com"))
        app.contact.submit_button()
        app.contact.open_home_page()
    app.contact.select_first_contact()
    app.contact.delete_button()
    app.contact.open_home_page()