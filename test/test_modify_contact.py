from model.contact import Contact
import random


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="Kseniya", lastname="Kurashova", nickname="KsiuSallivan",
                                        email="ksiu.sallivan@gmail.com", homephone="234234234",
                                        mobilephone="78", workphone="137699", secondaryphone="1243",
                                        email2='ksiu.sallivan2@gmail.com', email3="ksiu.sallivan3@gmail.com",
                                        address="SHJGhjd ds 24"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_fill = Contact(firstname="Candy", lastname="Twilight")
    app.contact.modify_contact_by_id(contact.id, contact_fill)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
