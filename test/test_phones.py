import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contacts_list()[1]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
    assert contact_from_home_page.all_phones_on_home_page == merge_phone_from_edit_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_on_home_page == merge_emails_from_edit_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address


'''
def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contacts_from_view_page(1)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
'''


def clear_phones(s):
    return re.sub("[-, ()]", "", s)


def clear_emails(s):
    return re.sub("[,()]", "", s)


def merge_phone_from_edit_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear_phones(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))


def merge_emails_from_edit_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear_emails(x),
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))
