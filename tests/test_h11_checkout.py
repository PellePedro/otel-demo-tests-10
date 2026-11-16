import json  # noqa: F401


def test_h11_9siqt8tojo_x4_pln_0001(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x5_ron_0002(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x10_rub_0003(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x1_sek_0004(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x2_sgd_0005(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x3_thb_0006(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x4_try_0007(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x5_usd_0008(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x10_zar_0009(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x1_aud_0010(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_9siqt8tojo_x2_bgn_0011(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("9SIQT8TOJO", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_6e92zmyyfz_x3_brl_0012(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("6E92ZMYYFZ", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_hqtgwgpnh4_x4_cad_0013(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("HQTGWGPNH4", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_oljcespc7z_x5_chf_0014(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("OLJCESPC7Z", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_66vchsjnup_x10_cny_0015(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("66VCHSJNUP", 10)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_1ymwwn1n4o_x1_czk_0016(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("1YMWWN1N4O", 1)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_l9ecav7kim_x2_dkk_0017(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("L9ECAV7KIM", 2)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_2zyfj3gm2n_x3_eur_0018(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("2ZYFJ3GM2N", 3)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_0puk6v6ev0_x4_gbp_0019(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("0PUK6V6EV0", 4)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []


def test_h11_ls4psxunum_x5_hkd_0020(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 200
    result = resp.json()
    assert result["orderId"]
    assert result["shippingTrackingId"]
    assert [(item["item"]["productId"], item["item"]["quantity"]) for item in result["items"]] == [("LS4PSXUNUM", 5)]
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.json()["items"] == []
