from model.contact import Contact


def test_contact_delete(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact("vova", "family", "last", "nick", "comp-2", "adr", "86665557744", "dfdf", "26",
                    "September", 2000))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete()
    app.driver.implicitly_wait(7)
    new_contant = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contant)
