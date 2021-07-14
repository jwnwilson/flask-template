def test_items_400(client):
    """Start with a blank database."""

    rv = client.get("/items")
    assert 401 == rv.status_code
