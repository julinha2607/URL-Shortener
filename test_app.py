import json
from app import create_app

def test_home_route():
    app = create_app()
    client = app.test_client()  # simula requisições
    response = client.get('/')
    assert response.status_code == 200
    assert b"Sua API" in response.data

def test_shorten_route():
    app = create_app()
    client = app.test_client()
    
    response = client.post('/shorten', 
        data=json.dumps({"url": "https://google.com"}),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert b"short_url" in response.data
