from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    # добавляем группу и контакт, если их нет
    if len(db.get_group_list()) == 0:
         app.group.create_group(Group(name="147", header="555", footer="666"))
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="Kseniya", email="ksiu.sallivan@gmail.com", homephone="234234234"))
    # берем группу, генерим для нее список контактов
    group = random.choice(db.get_group_list())
    old_group_content = orm.get_contacts_in_group(Group(id='%s' % group.id))
    # генерим новый контакт, если все в группах
    if len(db.contacts_id_without_group()) == 0:
        app.contact.create_contact(Contact(firstname="Kseniya", email="ksiu.sallivan@gmail.com", homephone="234234234"))
    # берем первый id из списка контактов без групп и по нему добавляем контакт в группу
    contact = db.contacts_id_without_group()[0]
    app.contact.add_contact_to_group(contact.id, group.id)
    old_group_content.append(contact)
    # генерим новый список контактов
    new_group_content = app.contact.see_group_content(group.id)
    # сверяем списки
    assert sorted(old_group_content, key=Contact.id_or_max) == sorted(new_group_content, key=Contact.id_or_max)



