# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

# Закомментировала часть, чтобы не генерилось 256 вариантов
testdata = [
        Contact(firstname=firstname,
                # lastname=lastname,
                #nickname=nickname,
                email=email,
                homephone=homephone
                # mobilephone=mobilephone, workphone=workphone,
                # secondaryphone=secondaryphone
                )
        for firstname in ["", random_string("firstname", 20)]
        # for lastname in ["", random_string("lastname", 20)]
        # for nickname in ["", random_string("nickname", 20)]
        for email in ["", random_string("email", 20)]
        for homephone in ["", random_string("home", 20)]
        # for mobilephone in ["", random_string("mobile", 20)]
        # for workphone in ["", random_string("work", 20)]
        # for secondaryphone in ["", random_string("phone2", 20)]
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
