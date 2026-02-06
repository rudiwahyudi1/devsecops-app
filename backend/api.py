def fetch_data(empty=False):
    if empty:
        return {}
    return {"status": "ok", "data": [1, 2, 3]}
