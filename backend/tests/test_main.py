import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "Backend OK 🚀"}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"health": "UP"}
