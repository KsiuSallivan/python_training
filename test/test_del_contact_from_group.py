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
    # group = random.choice(db.get_group_list())
    # if len(orm.get_contacts_in_group(Group(id='%s' % group.id))) == 0:
    #     group = random.choice(db.get_group_list())
    #     contact = orm.get_contacts_not_in_group(Group(id='%s' % group.id))[0]
    #     app.contact.add_contact_to_group(app.contact.add_contact_to_group(contact.id, group.id))
    # contact = orm.get_contacts_in_group(Group(id='%s' % group.id))[0]
    # генерим список контактов в группе
    # old_group_content = orm.get_contacts_in_group(Group(id='%s' % group.id))
    # удаляем контакт
    # app.contact.del_contact_from_group(contact.id, group.id)
    # обновляем список контактов в группе и генерим новый список контактов
    # old_group_content.remove(contact)
    # new_group_content = app.contact.see_group_content(group.id)
    # сверяем списки
    # assert sorted(old_group_content, key=Contact.id_or_max) == sorted(new_group_content, key=Contact.id_or_max)

# 2) В тесте удаления контакта из группы, аналогично вы проверяете случайную группу и если она не содержит контактов,
# то добавляете контакт в эту группу. Вместо этого можно было бы проверить другие группы, может быть есть такая,
# в которую добавлен хотя бы один контакт.

# def test_add_contact_to_group(app, db):

#     # берем группу, генерим для нее список контактов
#     group = random.choice(db.get_group_list())
#     old_group_content = orm.get_contacts_in_group(Group(id='%s' % group.id))
#     # генерим новый контакт, если все в группах
#     if len(db.contacts_id_without_group()) == 0:
#         app.contact.create_contact(Contact(firstname="Kseniya", email="ksiu.sallivan@gmail.com", homephone="234234234"))
#     # берем первый id из списка контактов без групп и по нему добавляем контакт в группу
#     contact = db.contacts_id_without_group()[0]
#     app.contact.add_contact_to_group(contact.id, group.id)
#     old_group_content.append(contact)
#     # генерим новый список контактов
#     new_group_content = app.contact.see_group_content(group.id)
#     # сверяем списки
#     assert sorted(old_group_content, key=Contact.id_or_max) == sorted(new_group_content, key=Contact.id_or_max)