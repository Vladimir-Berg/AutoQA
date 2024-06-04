import re
from fixture.orm import ORMFixture
from fixture.contact import Contact


def test_contacts_on_main_page(app):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    contacts_from_home_page = app.contact.get_contacts_list()
    contacts_from_db = db.get_contact_list()

    for item in contacts_from_db:
        item.all_phones_on_home_page = merge_phones(item)
        item.all_emails_on_home_page = merge_emails(item)

    #    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
    assert sorted(contacts_from_home_page, key=Contact.id_or_max) == sorted(contacts_from_db, key=Contact.id_or_max)
    for item in sorted(contacts_from_home_page, key=Contact.id_or_max):
        index = sorted(contacts_from_home_page, key=Contact.id_or_max).index(item)
        assert item.all_phones_on_home_page == sorted(contacts_from_db, key=Contact.id_or_max)[index].all_phones_on_home_page
        assert item.all_emails_on_home_page == sorted(contacts_from_db, key=Contact.id_or_max)[index].all_emails_on_home_page


def clear_phones(s):
    return re.sub("[-, ()]", "", s)


def clear_emails(s):
    return re.sub("[,()]", "", s)


def merge_phones(contact):
    return ''.join(filter(lambda x: x != '',
                            map(lambda x: clear_phones(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))


def merge_emails(contact):
    return ''.join(filter(lambda x: x != '',
                            map(lambda x: clear_emails(x),
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))
