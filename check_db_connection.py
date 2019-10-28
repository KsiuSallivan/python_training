import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group
from fixture.db import DbFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
# db = DbFixture

try:
    l = db.get_contacts_not_in_group(Group(id="192"))
    for item in l:
        print(l)
    print(len(l))
finally:
    pass #db.destroy()


# try:
#     l = db.get_contacts_in_group(Group(id="192"))
#     for item in l:
#         print(l)
#     print(len(l))
# finally:
#     pass #db.destroy()

# try:
#     l = db.get_contact_list()
#     for item in l:
#         print(l)
#     print(len(l))
# finally:
#     pass #db.destroy()


# try:
#     l = db.get_group_list()
#     for item in l:
#         print(l)
#     print(len(l))
# finally:
#     pass #db.destroy()