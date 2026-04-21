import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

def search_product_safe(name):
    # SECURE: Using ? placeholder - parameterised query
    query = "SELECT * FROM products WHERE name LIKE '%' || ? || '%'"
    print(f'Query: {query}')
    print(f'Parameter: {name}')
    rows = conn.execute(query, (name,)).fetchall()
    print(f'Result: {rows}\n')
    return rows

def login_safe(username, password):
    # SECURE: Using ? placeholders - parameterised query
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print(f'Query: {query}')
    print(f'Parameters: username={username}, password={password}')
    row = conn.execute(query, (username, password)).fetchone()
    print(f'Result: {row}\n')
    return row

# Test with the same attacks - they should all return empty results
print("=" * 60)
print("TEST 1: OR 1=1 attack (should return [])")
print("=" * 60)
print(search_product_safe("' OR 1=1--"))

print("=" * 60)
print("TEST 2: UNION attack (should return [])")
print("=" * 60)
print(search_product_safe("' UNION SELECT id,username,password,role FROM users--"))

print("=" * 60)
print("TEST 3: Admin bypass with comment (should return None)")
print("=" * 60)
print(login_safe("admin'--", "anything"))

print("=" * 60)
print("TEST 4: Always true login (should return None)")
print("=" * 60)
print(login_safe("' OR '1'='1", "' OR '1'='1"))

conn.close()