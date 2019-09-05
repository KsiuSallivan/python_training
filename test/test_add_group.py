# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.open_group_page()
    app.group.create_button()
    app.group.data_group(Group(name="147", header="555", footer="666"))
    app.group.submit_button()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
