from model.contact import Contact
from random import randrange


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Kseniya", lastname="Kurashova", nickname="KsiuSallivan",
                                           email="ksiu.sallivan@gmail.com"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Candy")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
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