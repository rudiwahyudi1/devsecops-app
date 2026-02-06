from backend.api import fetch_data

def test_fetch_data_success():
    result = fetch_data()
    assert isinstance(result, dict)
    assert "status" in result
    assert result["status"] == "ok"

def test_fetch_data_empty():
    result = fetch_data(empty=True)
    assert result == {}
