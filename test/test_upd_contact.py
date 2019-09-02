# -*- coding: utf-8 -*-
from model.contact import Contact


def test_upd_first_contact(app):
    app.contact.edit_button()
    app.contact.data_contact(Contact(firstname="Psh", lastname="HshHsh", nickname="Furfur",
                                     email="furfur@furfur.com"))
    app.contact.update_button()
    app.contact.open_home_page()
