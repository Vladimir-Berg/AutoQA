from model.contact import Contact


def test_contact_edit(app):
    app.contact.edit(Contact(firstname="VOVA-3"))
