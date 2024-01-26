def test_addcontact(app):
    app.session.login("admin", "secret")
    app.group.delete_first()
    app.session.logout()