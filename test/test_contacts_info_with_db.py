from model.contact import Contact
import re


# Задание 21
# для всех элементов
def test_contact_info_on_home_page_by_db(app, db):
    for contact_from_home_page in app.contact.get_contact_list():
        for contact_from_db in db.get_contact_list():
            if contact_from_home_page.id == contact_from_db.id:
                assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
                assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)
                assert contact_from_home_page.firstname == contact_from_db.firstname
                assert contact_from_home_page.lastname == contact_from_db.lastname
                assert contact_from_home_page.address == contact_from_db.address


# для первого элемента
# def test_contact_info_on_home_page_by_db(app, db):
#     contact_from_home_page = app.contact.get_contact_list()[0]
#     contact_from_db = db.get_contact_list()[0]
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
#     assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)
#     assert contact_from_home_page.firstname == contact_from_db.firstname
#     assert contact_from_home_page.lastname == contact_from_db.lastname
#     assert contact_from_home_page.address == contact_from_db.address


def twoinone(s):
    return re.sub('\\s+', '', s)


def clear(s):
    twoinone(s)
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact_from_db):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact_from_db.homephone, contact_from_db.mobilephone, contact_from_db.workphone,
                                        contact_from_db.secondaryphone]))))


def merge_emails_like_on_home_page(contact_from_db):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact_from_db.email, contact_from_db.email2,
                                        contact_from_db.email3]))))

