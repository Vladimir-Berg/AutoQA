from model.group import Group


def test_login_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group("Group", "Header", "Comment"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)