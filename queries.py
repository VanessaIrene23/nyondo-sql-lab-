import sqlite3

conn = sqlite3.connect('nyondo_stock.db')
cursor = conn.cursor()

print("=" * 50)
print("QUERY A: Get every column of every product")
print("=" * 50)
rows = cursor.execute('SELECT * FROM products').fetchall()
for row in rows:
    print(row)

print("\n" + "=" * 50)
print("QUERY B: Get only name and price of all products")
print("=" * 50)
rows = cursor.execute('SELECT name, price FROM products').fetchall()
for row in rows:
    print(f"Name: {row[0]}, Price: UGX {row[1]}")

print("\n" + "=" * 50)
print("QUERY C: Get full details of product with id = 3")
print("=" * 50)
# Note: Your current IDs start at 31, so id=31 is Cement
row = cursor.execute('SELECT * FROM products WHERE id = 31').fetchone()
print(row)

print("\n" + "=" * 50)
print("QUERY D: Find products whose name contains 'sheet'")
print("=" * 50)
rows = cursor.execute('SELECT * FROM products WHERE name LIKE "%sheet%"').fetchall()
for row in rows:
    print(row)

print("\n" + "=" * 50)
print("QUERY E: Get all products sorted by price, highest first")
print("=" * 50)
rows = cursor.execute('SELECT * FROM products ORDER BY price DESC').fetchall()
for row in rows:
    print(row)

print("\n" + "=" * 50)
print("QUERY F: Get only the 2 most expensive products")
print("=" * 50)
rows = cursor.execute('SELECT * FROM products ORDER BY price DESC LIMIT 2').fetchall()
for row in rows:
    print(row)

print("\n" + "=" * 50)
print("QUERY G: Update Cement price to 38,000 and confirm")
print("=" * 50)
# Update Cement (id=31)
cursor.execute('UPDATE products SET price = 38000 WHERE name LIKE "%Cement%"')
conn.commit()
row = cursor.execute('SELECT * FROM products WHERE name LIKE "%Cement%"').fetchone()
print(row)

conn.close()
