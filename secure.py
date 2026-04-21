import sqlite3

# Create a NEW connection (don't close it until the end)
conn = sqlite3.connect('nyondo_stock.db')

def validate_product_name(name):
    """Validate product name input"""
    if not isinstance(name, str):
        return False, "Name must be a string"
    if len(name) < 2:
        return False, "Name must be at least 2 characters"
    if '<' in name or '>' in name or ';' in name:
        return False, "Name cannot contain < > or ; characters"
    return True, "Valid"

def validate_username(username):
    """Validate username input"""
    if not isinstance(username, str):
        return False, "Username must be a string"
    if ' ' in username:
        return False, "Username cannot contain spaces"
    if len(username) == 0:
        return False, "Username cannot be empty"
    return True, "Valid"

def validate_password(password):
    """Validate password input"""
    if not isinstance(password, str):
        return False, "Password must be a string"
    if len(password) < 6:
        return False, "Password must be at least 6 characters"
    return True, "Valid"

def search_product_safe(name):
    # Input validation
    valid, message = validate_product_name(name)
    if not valid:
        print(f"Validation Error: {message}")
        print(f"Returning: []\n")
        return []
    
    # Parameterised query
    query = "SELECT * FROM products WHERE name LIKE '%' || ? || '%'"
    print(f'Query: {query}')
    print(f'Parameter: {name}')
    rows = conn.execute(query, (name,)).fetchall()
    print(f'Result: {rows}\n')
    return rows

def login_safe(username, password):
    # Input validation
    valid_u, msg_u = validate_username(username)
    if not valid_u:
        print(f"Validation Error: {msg_u}")
        print(f"Returning: None\n")
        return None
    
    valid_p, msg_p = validate_password(password)
    if not valid_p:
        print(f"Validation Error: {msg_p}")
        print(f"Returning: None\n")
        return None
    
    # Parameterised query
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print(f'Query: {query}')
    print(f'Parameters: username={username}, password={password}')
    row = conn.execute(query, (username, password)).fetchone()
    print(f'Result: {row}\n')
    return row

print("=" * 60)
print("TESTING SEARCH PRODUCT WITH VALIDATION")
print("=" * 60)

print("\n--- Test 1: search_product_safe('cement') - should work ---")
search_product_safe('cement')

print("\n--- Test 2: search_product_safe('') - should be rejected (too short) ---")
search_product_safe('')

print("\n--- Test 3: search_product_safe('<script>') - should be rejected (invalid chars) ---")
search_product_safe('<script>')

print("\n" + "=" * 60)
print("TESTING LOGIN WITH VALIDATION")
print("=" * 60)

print("\n--- Test 4: login_safe('admin', 'admin123') - should work ---")
login_safe('admin', 'admin123')

print("\n--- Test 5: login_safe('admin', 'ab') - should be rejected (password too short) ---")
login_safe('admin', 'ab')

print("\n--- Test 6: login_safe('ad min', 'pass123') - should be rejected (space in username) ---")
login_safe('ad min', 'pass123')

# Close connection at the very end
conn.close()
