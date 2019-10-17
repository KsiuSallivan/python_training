# -*- coding: utf-8 -*-
from model.group import Group
import allure


@allure.step('Given a group list')
def retrieve_old_list(db):
    old_groups = db.get_group_list()
    return old_groups


@allure.step('When I add a group %s to the list' % group)
def create_group(app, json_groups):
    group = json_groups
    app.group.create_group(group)

@allure.step('Then the new group list is equal to the old list with the added group')
def add_and_assert_groups(app, db, check_ui, json_groups):
    old_groups = retrieve_old_list()
    group = json_groups
    create_group()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# Старая версия
# def test_add_group(app, db, json_groups, check_ui):
#     group = json_groups
#     old_groups = db.get_group_list()
#     app.group.create_group(group)
#     new_groups = db.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#     if check_ui:
#         assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
