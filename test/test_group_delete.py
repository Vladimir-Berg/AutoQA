
def test_first_group_delete(app):
    app.session.login("admin", "secret")
    app.group.delete_first()
    app.session.logout()
