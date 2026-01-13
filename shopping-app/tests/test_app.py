import pytest
import sys
import os

# Add app directory to path so we can import app
sys.path.append(os.path.join(os.path.dirname(__file__), '../app'))

from app import app, init_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    # Use in-memory DB for testing
    # Note: Because models.py currently uses a hardcoded 'database.db' in current dir,
    # for cleaner testing we might want to refactor models.py to accept a db path config.
    # However, for this simple practice app, we will let it run but be aware of side effects 
    # or just simple route testing. To keep it simple and unintrusive, we'll just test the routes work.
    
    with app.test_client() as client:
        with app.app_context():
            init_db() # Ensure db exists
        yield client

def test_index_page(client):
    """Test that the index page loads."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"DevOps Shopping App" in response.data

def test_cart_page_empty(client):
    """Test that cart page loads."""
    response = client.get('/cart')
    assert response.status_code == 200
    assert b"Your Cart" in response.data
