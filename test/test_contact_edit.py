from model.contact import Contact


def test_contact_edit(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact("vova", "family", "last", "nick", "comp-2", "adr", "86665557744", "dfdf", "26",
                    "September", 2000))
    old_contacts = app.contact.get_contacts_list()
    app.contact.edit(Contact(firstname="VOVA-3"))
    new_contant = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contant)
