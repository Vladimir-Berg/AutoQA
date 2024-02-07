from model.group import Group


def test_group_edit(app):
    app.group.edit(Group(name="Group123"))
