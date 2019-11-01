from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_contact_from_group(app, db):
    # добавляем группу и контакт, если их нет
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="Kseniya", email="ksiu.sallivan@gmail.com", homephone="234234234"))
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name="147", header="555", footer="666"))
    # пробуем выбрать контакт и группу, либо создаем
    if len(db.groups_with_contacts()) == 0:
        group = db.groups_with_contacts()[0]
        contact = orm.get_contacts_in_group(Group(id='%s' % group.id))[0]
        app.contact.add_contact_to_group(contact.id, group.id)
    group = db.groups_with_contacts()[0]
    contact = orm.get_contacts_in_group(Group(id='%s' % group.id))[0]
    # генерим список контактов в группе
    old_group_content = orm.get_contacts_in_group(Group(id='%s' % group.id))
    # удаляем контакт
    app.contact.del_contact_from_group(contact.id, group.id)
    # обновляем список контактов в группе и генерим новый список контактов
    old_group_content.remove(contact)
    new_group_content = app.contact.see_group_content(group.id)
    # сверяем списки
    assert sorted(old_group_content, key=Contact.id_or_max) == sorted(new_group_content, key=Contact.id_or_max)
