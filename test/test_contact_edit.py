from model.contact import Contact


def test_contact_edit(app):
    app.session.login("admin", "secret")
    app.contact.edit(
        Contact("vova2", "family", "last", "nick", "comp-2", "adr", "86665557744", "dfdf", "//option[. = '26']",
                "//option[. = 'September']", 2000, "//option[. = 'Group2']"))
    app.session.logout()
