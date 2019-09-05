# -*- coding: utf-8 -*-
from model.contact import Contact


def test_upd_first_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create_button()
        app.contact.data_contact(Contact(firstname="Kseniya", lastname="Kurashova", nickname="KsiuSallivan",
                                         email="ksiu.sallivan@gmail.com"))
        app.contact.submit_button()
        app.open_home_page()
    app.contact.edit_button()
    app.contact.data_contact(Contact(firstname="Psh", lastname="HshHsh", nickname="Furfur",
                                     email="furfur@furfur.com"))
    app.contact.update_button()
