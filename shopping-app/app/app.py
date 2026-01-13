from flask import Flask, render_template, redirect, url_for
from models import init_db, get_db_connection

app = Flask(__name__)

# Initialize DB on startup (for simplicity in this demo)
# In production, this might be a separate command or check.
try:
    init_db()
except Exception as e:
    print(f"Error initializing DB: {e}")

@app.route('/')
def index():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return render_template('index.html', products=products)

@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    conn = get_db_connection()
    # Check if item already in cart
    item = conn.execute('SELECT * FROM cart WHERE product_id = ?', (product_id,)).fetchone()
    
    if item:
        conn.execute('UPDATE cart SET quantity = quantity + 1 WHERE id = ?', (item['id'],))
    else:
        conn.execute('INSERT INTO cart (product_id, quantity) VALUES (?, ?)', (product_id, 1))
    
    conn.commit()
    conn.close()
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    conn = get_db_connection()
    # Join cart and products to get names and prices
    cart_items = conn.execute('''
        SELECT c.id, c.quantity, p.name, p.price, (c.quantity * p.price) as total
        FROM cart c
        JOIN products p ON c.product_id = p.id
    ''').fetchall()
    
    grand_total = sum(item['total'] for item in cart_items)
    
    conn.close()
    return render_template('cart.html', cart_items=cart_items, grand_total=grand_total)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
