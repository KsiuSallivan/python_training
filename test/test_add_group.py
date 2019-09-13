# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="147", header="555", footer="666")
    app.group.create_group(group)
    # app.group.group_cache_none()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    # old_groups.append(group)
    # assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
