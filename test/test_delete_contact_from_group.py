import time
from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_in_group(app, db_orm):

    if len(db_orm.get_contact_list()) == 0:
        app.contact.create(
            Contact("Vladimir", "Vova-mid", "Berg", "Vova-nick", "CompStyleee", "Street 5 Home 6",
                    "8-666-555-77-44", "8(666)5557755", "8(666)5557766",
                    "email@gmail.com", "email@gmail.com", "email@gmail.com", "26", "September", 2000))

    if len(db_orm.get_groups_list()) == 0:
        app.group.create(Group("Group1", "Header1", "Footer1"))

    old_contacts = db_orm.get_contact_list()
    contact = random.choice(old_contacts)
    old_groups = db_orm.get_groups_list()
    group = random.choice(old_groups)

    if len(db_orm.get_contacts_in_group(group.id)) == 0:
        print('В группе нет контактов')
        print('Добавляем контакт ' + contact.id + ' в группу ' + group.id)
        app.contact.add_contact_in_group(contact.id, group.id)

    old_contacts_in_group = db_orm.get_contacts_in_group(group.id)
    contact = random.choice(old_contacts_in_group)
    app.contact.delete_contact_from_group(group.id, contact.id)
    new_contacts_in_group = db_orm.get_contacts_in_group(group.id)
    old_contacts_in_group.remove(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
