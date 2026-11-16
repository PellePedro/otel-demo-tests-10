import json  # noqa: F401


def test_h08_l9ecav7kim_0001(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_2zyfj3gm2n_0002(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_0puk6v6ev0_0003(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_ls4psxunum_0004(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_9siqt8tojo_0005(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_6e92zmyyfz_0006(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_hqtgwgpnh4_0007(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_oljcespc7z_0008(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_66vchsjnup_0009(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []


def test_h08_1ymwwn1n4o_0010(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.delete("/api/cart", json={"userId": user_id})
    assert resp.status_code == 204
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    assert resp.json()["items"] == []
