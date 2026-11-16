import json  # noqa: F401


def test_h10_no_address_0001(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "L9ECAV7KIM", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0002(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400


def test_h10_no_address_0003(api):
    resp = api.get("/api/shipping", params={'itemList': '[{"productId": "0PUK6V6EV0", "quantity": 1}]', 'currencyCode': 'USD'})
    assert resp.status_code >= 400


def test_h10_no_itemlist_0004(api):
    resp = api.get("/api/shipping", params={'currencyCode': 'USD', 'address': '{"streetAddress": "1600 Amphitheatre Parkway", "zipCode": "94043", "city": "Mountain View", "state": "CA", "country": "United States"}'})
    assert resp.status_code >= 400
