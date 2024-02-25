from model.group import Group


def test_first_group_delete(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group_1"))
    old_groups = app.group.get_group_list()
    app.group.delete_first()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups
