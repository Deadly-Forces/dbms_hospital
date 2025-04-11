import sqlite3

def connect_db():
    conn = sqlite3.connect('hospital.db')
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            blood_group TEXT NOT NULL,
            disease_type TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_patient(name, age, blood_group, disease_type):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO patients (name, age, blood_group, disease_type)
        VALUES (?, ?, ?, ?)
    ''', (name, age, blood_group, disease_type))
    conn.commit()
    conn.close()

def get_patients():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients')
    patients = cursor.fetchall()
    conn.close()
    return patients

def get_patient(patient_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients WHERE id = ?', (patient_id,))
    patient = cursor.fetchone()
    conn.close()
    return patient

def delete_patient(patient_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM patients WHERE id = ?', (patient_id,))
    conn.commit()
    conn.close()

def get_patients_by_disease(disease_type):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients WHERE disease_type LIKE ?', ('%' + disease_type + '%',))
    patients = cursor.fetchall()
    conn.close()
    return patients
def reset_database():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM patients')
    cursor.execute('DELETE FROM sqlite_sequence WHERE name="patients"')
    conn.commit()
    conn.close()
