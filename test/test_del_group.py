# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_delete_some_group(app):
    app.group.open_group_page()
    if app.group.count() == 0:
        app.group.create_button()
        app.group.data_group(Group(name="147", header="555", footer="666"))
        app.group.submit_button()
        app.group.open_group_page()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.select_group_by_index(index)
    app.group.delete_button()
    app.group.group_cache_none()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups
