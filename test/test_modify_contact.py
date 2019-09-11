from model.contact import Contact


def test_modify_contact_firstname(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create_button()
        app.contact.data_contact(Contact(firstname="Kseniya", lastname="Kurashova", nickname="KsiuSallivan",
                                         email="ksiu.sallivan@gmail.com"))
        app.contact.submit_button()
        app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Candy")
    contact.id = old_contacts[0].id
    app.contact.select_first_contact()
    app.contact.edit_button()
    app.contact.modify_first_contact(contact)
    app.contact.update_button()
    app.contact.contact_cache_none()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_contact_lastname(app):
#     app.open_home_page()
#     if app.contact.count() == 0:
#         app.contact.create_button()
#         app.contact.data_contact(Contact(firstname="Kseniya", lastname="Kurashova", nickname="KsiuSallivan",
#                                          email="ksiu.sallivan@gmail.com"))
#         app.contact.submit_button()
#         app.open_home_page()
#     app.contact.select_first_contact()
#     app.contact.edit_button()
#     app.contact.modify_first_contact(Contact(lastname="Twilight"))
#     app.contact.update_button()