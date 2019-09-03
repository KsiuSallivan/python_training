from model.group import Group


def test_modify_group_name(app):
    app.group.open_group_page()
    if app.group.count() == 0:
        app.group.create_button()
        app.group.data_group(Group(name="147", header="555", footer="665"))
        app.group.submit_button()
        app.group.open_group_page()
    app.group.select_first_group()
    app.group.edit_button()
    app.group.modify_first_group(Group(name="New funny name"))
    app.group.update_button()


def test_modify_group_header(app):
    app.group.open_group_page()
    if app.group.count() == 0:
        app.group.create_button()
        app.group.data_group(Group(name="147", header="555", footer="665"))
        app.group.submit_button()
        app.group.open_group_page()
    app.group.select_first_group()
    app.group.edit_button()
    app.group.modify_first_group(Group(header="New funny header"))
    app.group.update_button()