from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture


# 1. проверить, что есть контакт в группе через бд
# 2. сделать все, что в тесте на добавление, если такого нет
# 3. удалть контакт из группы через интерфейс
# 4. проверить что контакт удален через бд


orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_contact_from_group(app, db, orm):
    if len(orm.get_contacts_in_group()) == 0:
        if len(db.get_contact_list()) == 0:
            app.contact.create_contact(
                Contact(firstname="Kseniya", email="ksiu.sallivan@gmail.com", homephone="234234234"))
        if len(db.get_group_list()) == 0:
            app.group.create_group(Group(name="147", header="555", footer="666"))
        app.contact.add_contact_to_group(id)
    app.contact.del_contact_from_group(id)
    orm.get_contacts_not_in_group(Group(id="%s"))
