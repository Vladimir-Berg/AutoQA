from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None,
                 company=None, address=None,
                 homephone=None, mobilephone=None, workphone=None,
                 email1=None, email2=None, email3=None, bday=None, bmonth=None, byear=None,
                 all_phones_on_home_page=None, all_emails_on_home_page=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.all_phones_on_home_page = all_phones_on_home_page
        self.all_emails_on_home_page = all_emails_on_home_page
        self.id = id

    def __repr__(self):
        return "Contact(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % (
            self.firstname, self.lastname, self.id, self.middlename, self.nickname,
            self.company, self.address,
            self.homephone, self.mobilephone, self.workphone,
            self.email1, self.email2, self.email3,
            self.bday, self.bmonth, self.byear)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
