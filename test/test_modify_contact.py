from model.contact import Contact
from random import randrange


def test_modify_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Kseniya", lastname="Kurashova", nickname="KsiuSallivan",
                                                email="ksiu.sallivan@gmail.com", homephone="234234234",
                                                mobilephone="78", workphone="137699", secondaryphone="1243",
                                                email2='ksiu.sallivan2@gmail.com', email3="ksiu.sallivan3@gmail.com",
                                                address="SHJGhjd ds 24"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Candy", lastname="Twilight")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)