import json  # noqa: F401


def test_h05_6e92zmyyfz_x5_0001(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 5)]


def test_h05_hqtgwgpnh4_x10_0002(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 10)]


def test_h05_oljcespc7z_x1_0003(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 1)]


def test_h05_66vchsjnup_x2_0004(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 2)]


def test_h05_1ymwwn1n4o_x3_0005(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 3)]


def test_h05_l9ecav7kim_x4_0006(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 4)]


def test_h05_2zyfj3gm2n_x5_0007(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 5)]


def test_h05_0puk6v6ev0_x10_0008(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 10)]


def test_h05_ls4psxunum_x1_0009(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 1)]


def test_h05_9siqt8tojo_x2_0010(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 2)]


def test_h05_6e92zmyyfz_x3_0011(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 3)]


def test_h05_hqtgwgpnh4_x4_0012(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 4)]


def test_h05_oljcespc7z_x5_0013(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 5)]


def test_h05_66vchsjnup_x10_0014(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 10)]


def test_h05_1ymwwn1n4o_x1_0015(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 1)]


def test_h05_l9ecav7kim_x2_0016(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 2)]


def test_h05_2zyfj3gm2n_x3_0017(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 3)]


def test_h05_0puk6v6ev0_x4_0018(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 4)]


def test_h05_ls4psxunum_x5_0019(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 5)]


def test_h05_9siqt8tojo_x10_0020(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 10)]


def test_h05_6e92zmyyfz_x1_0021(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 1)]


def test_h05_hqtgwgpnh4_x2_0022(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 2)]


def test_h05_oljcespc7z_x3_0023(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 3)]


def test_h05_66vchsjnup_x4_0024(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 4)]


def test_h05_1ymwwn1n4o_x5_0025(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 5)]


def test_h05_l9ecav7kim_x10_0026(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 10)]


def test_h05_2zyfj3gm2n_x1_0027(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 1)]


def test_h05_0puk6v6ev0_x2_0028(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 2)]


def test_h05_ls4psxunum_x3_0029(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 3)]


def test_h05_9siqt8tojo_x4_0030(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 4)]


def test_h05_6e92zmyyfz_x5_0031(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("6E92ZMYYFZ", 5)]


def test_h05_hqtgwgpnh4_x10_0032(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("HQTGWGPNH4", 10)]


def test_h05_oljcespc7z_x1_0033(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("OLJCESPC7Z", 1)]


def test_h05_66vchsjnup_x2_0034(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("66VCHSJNUP", 2)]


def test_h05_1ymwwn1n4o_x3_0035(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 3}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("1YMWWN1N4O", 3)]


def test_h05_l9ecav7kim_x4_0036(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 4}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("L9ECAV7KIM", 4)]


def test_h05_2zyfj3gm2n_x5_0037(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 5}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("2ZYFJ3GM2N", 5)]


def test_h05_0puk6v6ev0_x10_0038(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 10}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("0PUK6V6EV0", 10)]


def test_h05_ls4psxunum_x1_0039(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("LS4PSXUNUM", 1)]


def test_h05_9siqt8tojo_x2_0040(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 2}})
    assert resp.status_code == 200
    resp = api.get("/api/cart", params={"sessionId": user_id})
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert [(item["productId"], item["quantity"]) for item in items] == [("9SIQT8TOJO", 2)]
