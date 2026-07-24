import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("payments.db")
    c = conn.cursor()

    c.execute("PRAGMA table_info(payments)")
    columns = c.fetchall()

    # If old structure exists (only 2 columns) → migrate
    if len(columns) not in (0, 4):
        c.execute("DROP TABLE IF EXISTS payments")

    c.execute('''CREATE TABLE IF NOT EXISTS payments
                 (name TEXT, upi TEXT, amount REAL, timestamp TEXT)''')

    conn.commit()
    conn.close()

def save_payment(name, upi, amount=0):
    conn = sqlite3.connect("payments.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO payments (name, upi, amount, timestamp) VALUES (?, ?, ?, ?)",
        (name, upi, amount, datetime.now().isoformat())
    )

    conn.commit()
    conn.close()

def get_payments():
    conn = sqlite3.connect("payments.db")
    c = conn.cursor()

    c.execute("SELECT * FROM payments")
    data = c.fetchall()

    conn.close()
    return data
