from model.group import Group
from random import randrange


def test_modify_group_name(app):
    app.group.open_group_page()
    if app.group.count() == 0:
        app.group.create_button()
        app.group.data_group(Group(name="147", header="555", footer="665"))
        app.group.submit_button()
        app.group.open_group_page()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New funny name")
    group.id = old_groups[index].id
    app.group.select_group_by_index(index)
    app.group.edit_button()
    app.group.modify_group(group)
    app.group.update_button()
    app.group.group_cache_none()
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#     app.group.open_group_page()
#     if app.group.count() == 0:
#         app.group.create_button()
#         app.group.data_group(Group(name="147", header="555", footer="665"))
#         app.group.submit_button()
#         app.group.open_group_page()
#     old_groups = app.group.get_group_list()
#     app.group.select_first_group()
#     app.group.edit_button()
#     app.group.modify_first_group(Group(header="New funny header"))
#     app.group.update_button()
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)