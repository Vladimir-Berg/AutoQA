import random

from model.contact import Contact
from random import randrange


def test_contact_delete(app, db):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(
            Contact("Vladimir", "Vova-mid", "Berg", "Vova-nick", "CompStyleee", "Street 5 Home 6",
                    "8-666-555-77-44", "8(666)5557755", "8(666)5557766",
                    "email@gmail.com", "email@gmail.com", "email@gmail.com", "26", "September", 2000))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    app.driver.implicitly_wait(7)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contacts_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
