from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_contact_from_group(app, db):
    # добавляем группу и контакт, если их нет
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="Kseniya", email="ksiu.sallivan@gmail.com", homephone="234234234"))
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name="147", header="555", footer="666"))
    # выбираем группу и контакт из нее, который надо удалить
    # добавляем контакт в группу, если его нет
    group = random.choice(db.get_group_list())
    if len(orm.get_contacts_in_group(Group(id='%s' % group.id))) == 0:
        group = random.choice(db.get_group_list())
        contact = orm.get_contacts_not_in_group(Group(id='%s' % group.id))[0]
        app.contact.add_contact_to_group(app.contact.add_contact_to_group(contact.id, group.id))
    contact = orm.get_contacts_in_group(Group(id='%s' % group.id))[0]
    # удаляем контакт
    app.contact.del_contact_from_group(contact.id, group.id)
    # app.contact.del_contact_from_group(256, 229)
    # добавляем проверки


