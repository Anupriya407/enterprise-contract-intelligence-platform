def test_search_endpoint_exists(client):
    response = client.get("/v1/documents/search?q=test")

    assert response.status_code == 200