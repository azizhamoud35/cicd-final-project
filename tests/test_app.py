import app


def test_index():
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode() == "SERVICE RUNNING"
