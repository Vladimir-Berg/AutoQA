from model.group import Group


def test_login_add_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("Group", "Header", "Comment"))
    app.session.logout()
    app.driver.close()
