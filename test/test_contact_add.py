from model.contact import Contact


def test_addcontact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact("vova", "family", "Фамилия", "nick", "comp-2", "adr", "86665557744", "dfdf", "26",
                      "September", 2000)
    app.contact.create(contact)
    new_contants = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contants)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contants, key=Contact.id_or_max)


"""def test_addcontact_1(app):
    app.contact.create(
        Contact("vova", "family", "last", "nick", "comp-2", "adr", "86665557744", "dfdf", "26",
                "September", 2000))"""
