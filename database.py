import sqlite3

def init_db():
    conn = sqlite3.connect("payments.db")
    c = conn.cursor()

    # Check existing columns
    c.execute("PRAGMA table_info(payments)")
    columns = c.fetchall()

    # If old structure exists → drop table
    if len(columns) != 2:
        c.execute("DROP TABLE IF EXISTS payments")

    # Create new table
    c.execute('''CREATE TABLE IF NOT EXISTS payments
                 (name TEXT, upi TEXT)''')

    conn.commit()
    conn.close()

def save_payment(name, upi):
    conn = sqlite3.connect("payments.db")
    c = conn.cursor()

    c.execute("INSERT INTO payments (name, upi) VALUES (?, ?)", (name, upi))

    conn.commit()
    conn.close()

def get_payments():
    conn = sqlite3.connect("payments.db")
    c = conn.cursor()

    c.execute("SELECT * FROM payments")
    data = c.fetchall()

    conn.close()
    return data