# -*- coding: utf-8 -*-

import unittest
import pytest
from model.contact import Contact
from fixture.application_contact import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Kseniya", lastname="Kurashova", nickname="KsiuSallivan",
                       email="ksiu.sallivan@gmail.com"))
    app.session.logout()


if __name__ == "__main__":
    unittest.main()
