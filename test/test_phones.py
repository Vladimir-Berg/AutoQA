import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contacts_list()[1]
    print(contact_from_home_page)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
    print(contact_from_edit_page)
    assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
    assert contact_from_home_page.mobilephone == clear(contact_from_edit_page.mobilephone)
    assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contacts_from_view_page(1)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone


def clear(s):
    return re.sub("[-, ()]", "", s)
