from model.contact import Contact
from model.group import Group
import random


def test_add_contact_in_group(app, db_orm):
    if len(db_orm.get_contact_list()) == 0:
        app.contact.create(
            Contact("Vladimir", "Vova-mid", "Berg", "Vova-nick", "CompStyleee", "Street 5 Home 6",
                    "8-666-555-77-44", "8(666)5557755", "8(666)5557766",
                    "email@gmail.com", "email@gmail.com", "email@gmail.com", "26", "September", 2000))

    if len(db_orm.get_groups_list()) == 0:
        app.group.create(Group("Group1", "Header1", "Footer1"))

    # Первый способ

    #    groups_list = app.contact.get_groups_from_list()
    #    empty_groups = check_empty_groups(db, groups_list)
    #    if len(empty_groups) == 0:
    #       group = Group('1', '1', '1')
    #       app.group.create(group)
    #       groups_list = app.contact.get_groups_from_list()
    #       empty_groups = check_empty_groups(db, groups_list)

    # Второй способ
    empty_groups = db_orm.get_groups_without_contacts()
    print('empty_groups', empty_groups)
    if len(empty_groups) == 0:
        group = Group('1', '1', '1')
        app.group.create(group)
        empty_groups = db_orm.get_groups_without_contacts()
        print('empty_groups', empty_groups)

    group = random.choice(empty_groups)
    old_contacts = db_orm.get_contact_list()
    contact = random.choice(old_contacts)

    # при первом способе вместо group.id указывать group_id
    old_contacts_in_group = db_orm.get_contacts_in_group(group.id)  # при первом способе вместо group.id указывать group_id
    app.contact.add_contact_in_group(contact.id, group.id)  # при первом способе вместо group.id указывать group_id
    new_contacts_in_group = db_orm.get_contacts_in_group(group.id)  # при первом способе вместо group.id указывать group_id

    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)


def check_empty_groups(db, groups_list):
    empty = []
    for item in groups_list:
        if len(db.get_contacts_in_group(item)) == 0:
            empty.append(item)
    return empty
