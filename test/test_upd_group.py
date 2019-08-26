# -*- coding: utf-8 -*-
from model.group import Group


def test_update_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.select_first_group()
    app.group.edit_button()
    app.group.data_group(Group(name="148", header="259", footer="360"))
    app.group.update_button()
    app.group.open_home_page()
    app.session.logout()