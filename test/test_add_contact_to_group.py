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
    # проверяем во взятой группе, что есть контакты, которые в нее не входят, и берем первый элемент
    group = random.choice(db.get_group_list())
    contact = orm.get_contacts_not_in_group(group)[0]
    # засовываем этот контакт в эту группу
    app.contact.add_contact_to_group(contact.id, group.id)
    # проверки - из дб и орм
    # старый список контактов в группе и получить новый список контактов в группе


