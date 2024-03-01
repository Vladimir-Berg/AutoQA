import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contacts_list()[1]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
    assert contact_from_home_page.all_phones_on_home_page == merge_phone_from_edit_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contacts_from_view_page(1)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone


def clear(s):
    return re.sub("[-, ()]", "", s)


def merge_phone_from_edit_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))
