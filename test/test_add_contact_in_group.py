from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture


def test_add_contact_in_group(app, db):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact("Vladimir", "Vova-mid", "Berg", "Vova-nick", "CompStyleee", "Street 5 Home 6",
                    "8-666-555-77-44", "8(666)5557755", "8(666)5557766",
                    "email@gmail.com", "email@gmail.com", "email@gmail.com", "26", "September", 2000))

    if len(db.get_groups_list()) == 0:
        app.group.create(Group("Group1", "Header1", "Footer1"))

    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    groups_list = app.contact.get_groups_from_list()
    group = random.choice(groups_list)
    old_contacts_in_group = db.get_contacts_in_group(group)
    app.contact.add_contact_in_group(contact.id, group)
    new_contacts_in_group = db.get_contacts_in_group(group)
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
