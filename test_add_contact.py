# -*- coding: utf-8 -*-

import unittest
import pytest
from contact import Contact
from application_contact import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Kseniya", lastname="Kurashova", nickname="KsiuSallivan",
                       email="ksiu.sallivan@gmail.com"))
    app.logout()


if __name__ == "__main__":
    unittest.main()
