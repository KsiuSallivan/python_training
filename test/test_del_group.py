# -*- coding: utf-8 -*-


def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.select_first_group()
    app.group.delete_button()
    app.group.open_home_page()
    app.session.logout()