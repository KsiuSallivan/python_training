from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture


# 1. проверить, что есть контакт через бд +
# 2. создать контакт, если его нет через интерфейс +
# 3. проверить, что есть группа через бд +
# 4. создать группу, если ее нет через интерфейс +
# 5. добавить контакт в группу через интерфейс ???
# 6. проверить, что контакт в группе через бд ???

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="Kseniya", email="ksiu.sallivan@gmail.com", homephone="234234234"))
    if len(db.get_group_list()) == 0:
         app.group.create_group(Group(name="147", header="555", footer="666"))
    app.contact.add_contact_to_group(id)
    orm.get_contacts_in_group(Group(id="%s"))


