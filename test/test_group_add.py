from model.group import Group


def test_login_add_group(app):
    app.group.create(Group("Group", "Header", "Comment"))
