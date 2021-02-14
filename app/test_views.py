def test_home_page(client):
    assert client.get(url_for("myview")).status_code == 200
