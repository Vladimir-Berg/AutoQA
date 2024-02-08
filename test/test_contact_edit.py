from model.contact import Contact


def test_contact_edit(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact("vova", "family", "last", "nick", "comp-2", "adr", "86665557744", "dfdf", "'26'",
                    "'September'", 2000))
    app.contact.edit(Contact(firstname="VOVA-3"))
