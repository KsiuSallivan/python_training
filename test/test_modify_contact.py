from model.contact import Contact


def test_modify_contact_firstname(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create_button()
        app.contact.data_contact(Contact(firstname="Kseniya", lastname="Kurashova", nickname="KsiuSallivan",
                                         email="ksiu.sallivan@gmail.com"))
        app.contact.submit_button()
        app.open_home_page()
    app.contact.select_first_contact()
    app.contact.edit_button()
    app.contact.modify_first_contact(Contact(firstname="Candy"))
    app.contact.update_button()


def test_modify_contact_lastname(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create_button()
        app.contact.data_contact(Contact(firstname="Kseniya", lastname="Kurashova", nickname="KsiuSallivan",
                                         email="ksiu.sallivan@gmail.com"))
        app.contact.submit_button()
        app.open_home_page()
    app.contact.select_first_contact()
    app.contact.edit_button()
    app.contact.modify_first_contact(Contact(lastname="Twilight"))
    app.contact.update_button()