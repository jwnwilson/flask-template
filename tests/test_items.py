def test_items_200(client):
    """Verify items endpoint."""

    rv = client.get("/items")
    assert 200 == rv.status_code
