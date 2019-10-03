from model.contact import Contact
import re


# Задание 21
def test_contact_info_on_home_page_by_db(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    # assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)
    # assert contact_from_home_page.all_phones_from_home_page == contact_from_db.all_phones_from_home_page
    # assert contact_from_home_page.all_emails_from_home_page == contact_from_db.all_emails_from_home_page
    assert contact_from_home_page.firstname == contact_from_db.firstname
    assert contact_from_home_page.lastname == contact_from_db.lastname
    assert contact_from_home_page.address == contact_from_db.address


def twoinone(s):
    return re.sub('\s+', '', s)


def clear(s):
    twoinone(s)
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone,
                                        contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2,
                                        contact.email3]))))
