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
    # проверяем во взятой группе, что есть контакты, которые в нее не входят, добавляем новый в случае чего,
    # сохраняем список контактов взятой группы и берем первый элемент
    group = random.choice(db.get_group_list())
    old_group_content = orm.get_contacts_in_group(Group(id='%s' % group.id))
    print(old_group_content)
    try:
        if len(orm.get_contacts_not_in_group(Group(id='%s' % group.id))) == 0:
            app.contact.create_contact(Contact(firstname="Kseniya", email="ksiu.sallivan@gmail.com", homephone="234234234"))
    except:
        pass
    contact = orm.get_contacts_not_in_group(Group(id='%s' % group.id))[0]
    # засовываем полученный контакт в полученную группу, обновляем список контактов в группе
    # и генерим новый список контактов
    app.contact.add_contact_to_group(contact.id, group.id)
    old_group_content.append(contact)
    print(old_group_content)
    new_group_content = app.contact.see_group_content(group.id)
    print(new_group_content)
    # сверяем списки
    assert sorted(old_group_content, key=Contact.id_or_max) == sorted(new_group_content, key=Contact.id_or_max)



