from model.contact import Contact


def test_contact_edit(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact("vova", "family", "last", "nick", "comp-2", "adr", "86665557744", "dfdf", "26",
                    "September", 2000))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="VOVA-4")
    contact.id = old_contacts[0].id
    app.contact.edit(contact)
    new_contants = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contants)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contants, key=Contact.id_or_max)
