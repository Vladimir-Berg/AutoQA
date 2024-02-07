from model.contact import Contact


def test_addcontact(app):
    app.contact.create(
        Contact("vova", "family", "last", "nick", "comp-2", "adr", "86665557744", "dfdf", "'26'",
                "'September'", 2000))


def test_addcontact_1(app):
    app.contact.create(
        Contact("vova", "family", "last", "nick", "comp-2", "adr", "86665557744", "dfdf", "'26'",
                "'September'", 2000))
