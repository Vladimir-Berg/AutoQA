from model.contact import Contact


def test_contact_edit(app):
    app.session.login("admin", "secret")
    app.contact.edit(Contact(firstname="VOVA-3"))
    app.session.logout()
