from model.contact import Contact


def test_addcontact(app):
    app.session.login("admin", "secret")
    app.contact.create(
        Contact("vova", "family", "last", "nick", "comp-2", "adr", "86665557744", "dfdf", "//option[. = '26']",
                "'September'", 2000, "//option[. = 'Group2']"))
    app.session.logout()
