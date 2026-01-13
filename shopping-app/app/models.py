import sqlite3
import os

DB_NAME = "database.db"

def init_db():
    """Initialize the database with products and cart tables."""
    # Check if database exists, if not create it
    if not os.path.exists(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Create Products table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                image TEXT
            )
        ''')

        # Create Cart table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cart (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                FOREIGN KEY (product_id) REFERENCES products (id)
            )
        ''')

        # Seed initial data if empty
        cursor.execute('SELECT count(*) FROM products')
        if cursor.fetchone()[0] == 0:
            products = [
                ('Laptop', 999.99, 'laptop.jpg'),
                ('Headphones', 199.99, 'headphones.jpg'),
                ('Mouse', 29.99, 'mouse.jpg'),
                ('Keyboard', 59.99, 'keyboard.jpg'),
                ('Monitor', 249.99, 'monitor.jpg')
            ]
            cursor.executemany('INSERT INTO products (name, price, image) VALUES (?, ?, ?)', products)
            print("Database seeded with initial products.")

        conn.commit()
        conn.close()
        print("Database initialized.")

def get_db_connection():
    """Create a database connection."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

if __name__ == '__main__':
    init_db()
