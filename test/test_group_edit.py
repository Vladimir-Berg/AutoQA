from model.group import Group


def test_group_edit(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group_for_edit"))
    old_groups = app.group.get_group_list()
    app.group.edit(Group(name="Group123"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

