from pony.orm import *
from model.group import Group
from model.contact import Contact


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column="firstname")
        lastname = Optional(str, column='lastname')
        middlename = Optional(str, column="middlename")
        nickname = Optional(str, column="nickname")
        company = Optional(str, column="company")
        address = Optional(str, column="address")
        homephone = Optional(str, column="home")
        mobilephone = Optional(str, column="mobile")
        workphone = Optional(str, column="work")
        email1 = Optional(str, column="email")
        email2 = Optional(str, column="email2")
        email3 = Optional(str, column="email3")
        bday = Optional(str, column="bday")
        bmonth = Optional(str, column="bmonth")
        byear = Optional(str, column="byear")

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, db=name, user=user, passwd=password)
        self.db.generate_mapping()

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)

        return list(map(convert, groups))

    @db_session
    def get_groups_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname,
                           middlename=contact.middlename, nickname=contact.nickname,
                           company=contact.company, address=contact.address,
                           homephone=contact.homephone, mobilephone=contact.mobilephone, workphone=contact.workphone,
                           email1=contact.email1, email2=contact.email2, email3=contact.email3,
                           bday=contact.bday, bmonth=contact.bmonth, byear=contact.byear)

        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact))
