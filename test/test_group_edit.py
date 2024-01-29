from model.group import Group


def test_group_edit(app):
    app.session.login("admin", "secret")
    app.group.edit(Group("Group123", "Header123", "Comment123"))
    app.session.logout()
