from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture

# Для второго теста надо проверять, что существуют контакты, которые можно удалить из группы (и добавлять контакт в
# группу если все контакты удалены из всех групп).

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_contact_from_group(app, db):
    # добавляем группу и контакт, если их нет
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="Kseniya", email="ksiu.sallivan@gmail.com", homephone="234234234"))
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name="147", header="555", footer="666"))
    # app.contact.add_contact_to_group(id)
    app.contact.del_contact_from_group(242, 202)

