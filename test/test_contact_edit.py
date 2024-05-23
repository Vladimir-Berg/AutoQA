from model.contact import Contact
import random


def test_contact_edit(app, db):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(
            Contact("Vladimir", "Vova-mid", "Berg", "Vova-nick", "CompStyleee", "Street 5 Home 6",
                    "8-666-555-77-44", "8(666)5557755", "8(666)5557766",
                    "email@gmail.com", "email@gmail.com", "email@gmail.com", "26", "September", 2000))
    old_contacts = db.get_contacts_list()
    contact_choice = random.choice(old_contacts)
    contact = Contact(firstname="7575755")
    contact.id = contact_choice.id
    app.contact.edit_contact_by_id(contact.id, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contacts_list()
    old_contacts.remove(contact_choice)
    old_contacts.append(contact)
#    old_contacts[old_contacts.index(contact_choice)] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
