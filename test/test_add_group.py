# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="147", header="555", footer="666")
    app.group.open_group_page()
    app.group.create_button()
    app.group.data_group(group)
    app.group.submit_button()
    app.group.group_cache_none()
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
