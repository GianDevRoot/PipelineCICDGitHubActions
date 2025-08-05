import sys
import os

# Añadir el directorio padre al path (para GitHub Actions)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask_app import app

def test_homepage():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hola Mundo" in response.data