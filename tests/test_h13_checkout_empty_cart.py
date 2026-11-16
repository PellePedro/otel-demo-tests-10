import json  # noqa: F401


def test_h13_mxn_0001(api, user_id):
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 500
    assert resp.json() == {"error": "Failed to place order."}


def test_h13_myr_0002(api, user_id):
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 500
    assert resp.json() == {"error": "Failed to place order."}


def test_h13_nok_0003(api, user_id):
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 500
    assert resp.json() == {"error": "Failed to place order."}


def test_h13_nzd_0004(api, user_id):
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 500
    assert resp.json() == {"error": "Failed to place order."}


def test_h13_php_0005(api, user_id):
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 500
    assert resp.json() == {"error": "Failed to place order."}
