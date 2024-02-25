from model.group import Group


def test_group_edit(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group_for_edit"))
    old_groups = app.group.get_group_list()
    group = Group(name="Group123")
    group.id = old_groups[0].id
    app.group.edit(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
