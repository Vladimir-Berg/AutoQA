from model.contact import Contact


def test_addcontact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact("Vladimir", "Vova-mid", "Berg", "Vova-nick", "CompStyleee", "Street 5 Home 6",
                      "8-666-555-77-44", "8(666)5557755", "8(666)5557766",
                      "email@gmail.com", "26", "September", 2000)
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contants = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contants, key=Contact.id_or_max)


"""def test_addcontact_1(app):
    app.contact.create(
        Contact("vova", "family", "last", "nick", "comp-2", "adr", "86665557744", "dfdf", "26",
                "September", 2000))"""
