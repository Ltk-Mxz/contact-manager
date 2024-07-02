import sqlite3

class Database:
    def __init__(self, db_name='contacts.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        create_table_sql = '''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE,
                email TEXT
            )
        '''
        self.cursor.execute(create_table_sql)
        self.connection.commit()

    def insert_contact(self, name, phone, email=None):
        try:
            insert_sql = '''
                INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)
            '''
            self.cursor.execute(insert_sql, (name, phone, email))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def fetch_contacts(self):
        fetch_sql = '''
            SELECT * FROM contacts
        '''
        self.cursor.execute(fetch_sql)
        return self.cursor.fetchall()

    def update_contact(self, contact_id, name, phone, email=None):
        try:
            update_sql = '''
                UPDATE contacts SET name=?, phone=?, email=? WHERE id=?
            '''
            self.cursor.execute(update_sql, (name, phone, email, contact_id))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def delete_contact(self, contact_id):
        delete_sql = '''
            DELETE FROM contacts WHERE id=?
        '''
        self.cursor.execute(delete_sql, (contact_id,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()