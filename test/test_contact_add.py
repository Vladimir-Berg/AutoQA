from model.contact import Contact
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + '' * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_of_direct(prefix, maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_of_months(prefix):
    symbols = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
    return random.choice(symbols)


testdata = [Contact(firstname='', middlename='', lastname='', nickname='', company='', address='',
                    homephone='', mobilephone='', workphone='', email1='', email2='', email3='',
                    bday='', bmonth='', byear='')] + [
               Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20),
                       lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                       company=random_string("company", 10), address=random_string("address", 20),
                       homephone=random_string("homephone", 10), mobilephone=random_string("mobilephone", 10, ),
                       workphone=random_string("workphone", 10), email1=random_string("email1", 10),
                       email2=random_string("email2", 10), email3=random_string("email3", 20),
                       bday=str(random_string_of_direct("bday", 2)), bmonth=random_string_of_months("bmonth"),
                       byear=random_string_of_direct("byear", 4)
                       )
               for i in range(5)
           ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_addcontact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contants = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contants, key=Contact.id_or_max)


"""def test_addcontact_1(app):
    app.contact.create(
        Contact("vova", "family", "last", "nick", "comp-2", "adr", "86665557744", "dfdf", "26",
                "September", 2000))"""
