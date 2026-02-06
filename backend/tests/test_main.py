from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    # Kirim GET request ke endpoint root
    response = client.get("/")

    # Pastikan status code 200 OK
    assert response.status_code == 200

    # Pastikan response JSON ada key 'status'
    json_data = response.json()
    assert "status" in json_data

    # Pastikan value sesuai dengan yang di-return backend
    assert json_data["status"] == "Backend OK 🚀"
