from model.group import Group
import random


def test_modify_first_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name="147", header="555", footer="666"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_fill = Group(name="New funny name")
    app.group.modify_group_by_id(group.id, group_fill)
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

