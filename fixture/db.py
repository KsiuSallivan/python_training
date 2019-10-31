import pymysql
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, nickname, address, home, mobile, work, email, email2,"
                           " email3, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, nickname, address, home, mobile, work, email, email2, email3, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, nickname=nickname,
                                    address=address, homephone=home, mobilephone=mobile, workphone=work,
                                    email=email, email2=email2, email3=email3, secondaryphone=phone2))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def contacts_with_group(self):
        list_c_with_g = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, group_id) = row
                list_c_with_g.append(Contact(id=str(id)))
        finally:
            cursor.close()
        return list_c_with_g

    def contacts_id_without_group(self):
        list_all = self.get_contact_list()
        list_c_with_g = self.contacts_with_group()
        list_c_without_g = []
        for c in list_all:
            found = False
            for c_g in list_c_with_g:
                if c.id == c_g.id:
                    found = True
            if not found:
                list_c_without_g.append(Contact(id=c.id, firstname=c.firstname))
        return list_c_without_g

    def groups_with_contacts(self):
        list_g_with_c = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (group_id) = row
                list_g_with_c.append(Group(id=group_id))
        finally:
            cursor.close()
        return list_g_with_c
