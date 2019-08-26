# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.create_button()
    app.group.data_group(Group(name="444", header="555", footer="666"))
    app.group.submit_button()
    app.group.open_home_page()
    app.session.logout()