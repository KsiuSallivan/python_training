# -*- coding: utf-8 -*-


def test_delete_first_contact(app):
    app.contact.select_first_contact()
    app.contact.delete_button()
    app.contact.open_home_page()