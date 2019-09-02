from model.group import Group


def test_modify_group_name(app):
    app.group.open_group_page()
    app.group.select_first_group()
    app.group.edit_button()
    app.group.modify_first_group(Group(name="New group"))
    app.group.update_button()


def test_modify_group_header(app):
    app.group.open_group_page()
    app.group.select_first_group()
    app.group.edit_button()
    app.group.modify_first_group(Group(header="New group"))
    app.group.update_button()