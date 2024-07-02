import pytest
from database import Database

@pytest.fixture
def db():
    database = Database(':memory:')  # Utilisation d'une base de données en mémoire pour les tests
    yield database
    del database

def test_add_contact(db):
    db.insert_contact('John Doe', '1234567890', 'john@example.com')
    contacts = db.fetch_contacts()
    assert len(contacts) == 1
    assert contacts[0][1] == 'John Doe'

def test_update_contact(db):
    db.insert_contact('Jane Doe', '0987654321', 'jane@example.com')
    contacts = db.fetch_contacts()
    contact_id = contacts[0][0]
    db.update_contact(contact_id, 'Jane Smith', '1112223333', 'jane.smith@example.com')
    updated_contacts = db.fetch_contacts()
    assert updated_contacts[0][1] == 'Jane Smith'

def test_delete_contact(db):
    db.insert_contact('Jake Doe', '5555555555', 'jake@example.com')
    contacts = db.fetch_contacts()
    contact_id = contacts[0][0]
    db.delete_contact(contact_id)
    updated_contacts = db.fetch_contacts()
    assert len(updated_contacts) == 0