from model.contact import Contact
import random
import string
import pytest



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
