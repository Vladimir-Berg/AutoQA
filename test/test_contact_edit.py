from model.contact import Contact
from random import randrange


def test_contact_edit(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact("Vladimir", "Vova-mid", "Berg", "Vova-nick", "CompStyleee", "Street 5 Home 6",
                    "8-666-555-77-44", "8(666)5557755", "8(666)5557766",
                    "email@gmail.com", "26", "September", 2000))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="AAAAAAAAAAAAAAAAAA")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contants = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contants, key=Contact.id_or_max)
