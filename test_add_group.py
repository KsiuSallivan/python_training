# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="111", header="222", footer="333"))
    app.logout()


if __name__ == "__main__":
    unittest.main()