from model.group import Group
import random


def test_group_edit(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Group_for_edit"))
    old_groups = db.get_group_list()
    group_choice = random.choice(old_groups)
    group = Group(name="6565")
    group.id = group_choice.id
    app.group.edit_group_by_id(group.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
#    old_groups.remove(group_choice)
#    old_groups.append(group)
    old_groups[old_groups.index(group_choice)] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
