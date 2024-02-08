from model.group import Group


def test_first_group_delete(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group_1"))
    app.group.delete_first()
