from model.group import Group


def test_first_group_delete(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group_1"))
    old_groups = app.group.get_group_list()
    app.group.delete_first()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)

