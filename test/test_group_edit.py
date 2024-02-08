from model.group import Group


def test_group_edit(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group_for_edit"))
    app.group.edit(Group(name="Group123"))
