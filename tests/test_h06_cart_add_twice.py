import json  # noqa: F401


def test_h06_6e92zmyyfz_x3_0001(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 6)]


def test_h06_hqtgwgpnh4_x4_0002(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 8)]


def test_h06_oljcespc7z_x5_0003(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 10)]


def test_h06_66vchsjnup_x10_0004(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 20)]


def test_h06_1ymwwn1n4o_x1_0005(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 2)]


def test_h06_l9ecav7kim_x2_0006(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 4)]


def test_h06_2zyfj3gm2n_x3_0007(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 6)]


def test_h06_0puk6v6ev0_x4_0008(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 8)]


def test_h06_ls4psxunum_x5_0009(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 10)]


def test_h06_9siqt8tojo_x10_0010(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 20)]


def test_h06_6e92zmyyfz_x1_0011(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 2)]


def test_h06_hqtgwgpnh4_x2_0012(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 4)]


def test_h06_oljcespc7z_x3_0013(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 6)]


def test_h06_66vchsjnup_x4_0014(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 8)]


def test_h06_1ymwwn1n4o_x5_0015(api, user_id):
    for _ in range(2):
        resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
        assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 10)]
