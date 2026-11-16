import json  # noqa: F401


def test_h14_oljcespc7z_pln_0001(api):
    resp = api.get("/api/recommendations", params={"productIds": ["OLJCESPC7Z"], "currencyCode": "PLN"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "OLJCESPC7Z" not in [product["id"] for product in products]


def test_h14_66vchsjnup_ron_0002(api):
    resp = api.get("/api/recommendations", params={"productIds": ["66VCHSJNUP"], "currencyCode": "RON"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "66VCHSJNUP" not in [product["id"] for product in products]


def test_h14_1ymwwn1n4o_rub_0003(api):
    resp = api.get("/api/recommendations", params={"productIds": ["1YMWWN1N4O"], "currencyCode": "RUB"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "1YMWWN1N4O" not in [product["id"] for product in products]


def test_h14_l9ecav7kim_sek_0004(api):
    resp = api.get("/api/recommendations", params={"productIds": ["L9ECAV7KIM"], "currencyCode": "SEK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "L9ECAV7KIM" not in [product["id"] for product in products]


def test_h14_2zyfj3gm2n_sgd_0005(api):
    resp = api.get("/api/recommendations", params={"productIds": ["2ZYFJ3GM2N"], "currencyCode": "SGD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "2ZYFJ3GM2N" not in [product["id"] for product in products]


def test_h14_0puk6v6ev0_thb_0006(api):
    resp = api.get("/api/recommendations", params={"productIds": ["0PUK6V6EV0"], "currencyCode": "THB"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "0PUK6V6EV0" not in [product["id"] for product in products]


def test_h14_ls4psxunum_try_0007(api):
    resp = api.get("/api/recommendations", params={"productIds": ["LS4PSXUNUM"], "currencyCode": "TRY"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "LS4PSXUNUM" not in [product["id"] for product in products]


def test_h14_9siqt8tojo_usd_0008(api):
    resp = api.get("/api/recommendations", params={"productIds": ["9SIQT8TOJO"], "currencyCode": "USD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "9SIQT8TOJO" not in [product["id"] for product in products]


def test_h14_6e92zmyyfz_zar_0009(api):
    resp = api.get("/api/recommendations", params={"productIds": ["6E92ZMYYFZ"], "currencyCode": "ZAR"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "6E92ZMYYFZ" not in [product["id"] for product in products]


def test_h14_hqtgwgpnh4_aud_0010(api):
    resp = api.get("/api/recommendations", params={"productIds": ["HQTGWGPNH4"], "currencyCode": "AUD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "HQTGWGPNH4" not in [product["id"] for product in products]


def test_h14_oljcespc7z_bgn_0011(api):
    resp = api.get("/api/recommendations", params={"productIds": ["OLJCESPC7Z"], "currencyCode": "BGN"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "OLJCESPC7Z" not in [product["id"] for product in products]


def test_h14_66vchsjnup_brl_0012(api):
    resp = api.get("/api/recommendations", params={"productIds": ["66VCHSJNUP"], "currencyCode": "BRL"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "66VCHSJNUP" not in [product["id"] for product in products]


def test_h14_1ymwwn1n4o_cad_0013(api):
    resp = api.get("/api/recommendations", params={"productIds": ["1YMWWN1N4O"], "currencyCode": "CAD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "1YMWWN1N4O" not in [product["id"] for product in products]


def test_h14_l9ecav7kim_chf_0014(api):
    resp = api.get("/api/recommendations", params={"productIds": ["L9ECAV7KIM"], "currencyCode": "CHF"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "L9ECAV7KIM" not in [product["id"] for product in products]


def test_h14_2zyfj3gm2n_cny_0015(api):
    resp = api.get("/api/recommendations", params={"productIds": ["2ZYFJ3GM2N"], "currencyCode": "CNY"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "2ZYFJ3GM2N" not in [product["id"] for product in products]


def test_h14_0puk6v6ev0_czk_0016(api):
    resp = api.get("/api/recommendations", params={"productIds": ["0PUK6V6EV0"], "currencyCode": "CZK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "0PUK6V6EV0" not in [product["id"] for product in products]


def test_h14_ls4psxunum_dkk_0017(api):
    resp = api.get("/api/recommendations", params={"productIds": ["LS4PSXUNUM"], "currencyCode": "DKK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "LS4PSXUNUM" not in [product["id"] for product in products]


def test_h14_9siqt8tojo_eur_0018(api):
    resp = api.get("/api/recommendations", params={"productIds": ["9SIQT8TOJO"], "currencyCode": "EUR"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "9SIQT8TOJO" not in [product["id"] for product in products]


def test_h14_6e92zmyyfz_gbp_0019(api):
    resp = api.get("/api/recommendations", params={"productIds": ["6E92ZMYYFZ"], "currencyCode": "GBP"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "6E92ZMYYFZ" not in [product["id"] for product in products]


def test_h14_hqtgwgpnh4_hkd_0020(api):
    resp = api.get("/api/recommendations", params={"productIds": ["HQTGWGPNH4"], "currencyCode": "HKD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "HQTGWGPNH4" not in [product["id"] for product in products]


def test_h14_oljcespc7z_hrk_0021(api):
    resp = api.get("/api/recommendations", params={"productIds": ["OLJCESPC7Z"], "currencyCode": "HRK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "OLJCESPC7Z" not in [product["id"] for product in products]


def test_h14_66vchsjnup_huf_0022(api):
    resp = api.get("/api/recommendations", params={"productIds": ["66VCHSJNUP"], "currencyCode": "HUF"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "66VCHSJNUP" not in [product["id"] for product in products]


def test_h14_1ymwwn1n4o_idr_0023(api):
    resp = api.get("/api/recommendations", params={"productIds": ["1YMWWN1N4O"], "currencyCode": "IDR"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "1YMWWN1N4O" not in [product["id"] for product in products]


def test_h14_l9ecav7kim_ils_0024(api):
    resp = api.get("/api/recommendations", params={"productIds": ["L9ECAV7KIM"], "currencyCode": "ILS"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "L9ECAV7KIM" not in [product["id"] for product in products]


def test_h14_2zyfj3gm2n_inr_0025(api):
    resp = api.get("/api/recommendations", params={"productIds": ["2ZYFJ3GM2N"], "currencyCode": "INR"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "2ZYFJ3GM2N" not in [product["id"] for product in products]
