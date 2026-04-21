import sqlite3

# Connect to database
conn = sqlite3.connect('nyondo_stock.db')
cursor = conn.cursor()

# Create products table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL
)
''')

# Delete duplicate products (keep only first 5)
cursor.execute('DELETE FROM products WHERE id > 5')

# Insert all 5 products (using INSERT OR IGNORE to avoid duplicates)
products = [
    ('Cement (bag)', 'Portland cement 50kg bag', 35000),
    ('Iron Sheet 3m', 'Gauge 30 roofing sheet 3m long', 110000),
    ('Paint 5L', 'Exterior wall paint white 5L', 60000),
    ('Nails 1kg', 'Common wire nails 1kg pack', 12000),
    ('Timber 2x4', 'Pine timber plank 2x4 per metre', 25000)
]

cursor.executemany('INSERT OR IGNORE INTO products (name, description, price) VALUES (?, ?, ?)', products)
conn.commit()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT DEFAULT 'attendant'
)
''')

# Insert users
users_data = [
    ('admin', 'admin123', 'admin'),
    ('fatuma', 'pass456', 'attendant'),
    ('wasswa', 'pass789', 'manager')
]

cursor.executemany('INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)', users_data)
conn.commit()

# Verify products
print("=== All Products ===")
rows = cursor.execute('SELECT * FROM products').fetchall()
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Description: {row[2]}, Price: UGX {row[3]}")

# Verify users
print("\n=== Users Table ===")
users = cursor.execute('SELECT * FROM users').fetchall()
for user in users:
    print(f"ID: {user[0]}, Username: {user[1]}, Password: {user[2]}, Role: {user[3]}")

# Close connection at the VERY END
conn.close()
