# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create_button()
    app.contact.data_contact(Contact(firstname="Kseniya", lastname="Kurashova", nickname="KsiuSallivan",
                                     email="ksiu.sallivan@gmail.com"))
    app.contact.submit_button()
    app.contact.open_home_page()
