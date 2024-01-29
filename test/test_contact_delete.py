def test_addcontact(app):
    app.session.login("admin", "secret")
    app.contact.delete()
    app.session.logout()