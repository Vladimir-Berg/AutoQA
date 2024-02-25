from model.contact import Contact


def test_addcontact(app):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(
        Contact("vova", "family", "Фамилия", "nick", "comp-2", "adr", "86665557744", "dfdf", "26",
                "September", 2000))
    new_contant = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contant)


"""def test_addcontact_1(app):
    app.contact.create(
        Contact("vova", "family", "last", "nick", "comp-2", "adr", "86665557744", "dfdf", "26",
                "September", 2000))"""
