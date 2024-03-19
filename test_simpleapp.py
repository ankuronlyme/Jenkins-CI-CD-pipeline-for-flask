import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert b'Hello, World! My Jenkins CI/CD pipeline for flask application.' in response.data






#import pytest
#from app import Hello, World! My Jenkins CI/CD pipeline for flask application.

#def test_Hello, World! My Jenkins CI/CD pipeline for flask application.():
 #   assert Hello, World! My Jenkins CI/CD pipeline for flask application.() == 'Hello, World! My Jenkins CI/CD pipeline for flask application.'



