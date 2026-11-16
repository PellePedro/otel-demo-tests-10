import json  # noqa: F401


def test_h02_ils_0001(api):
    resp = api.get("/api/products", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h02_inr_0002(api):
    resp = api.get("/api/products", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "INR"


def test_h02_isk_0003(api):
    resp = api.get("/api/products", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h02_jpy_0004(api):
    resp = api.get("/api/products", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h02_krw_0005(api):
    resp = api.get("/api/products", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h02_mxn_0006(api):
    resp = api.get("/api/products", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h02_myr_0007(api):
    resp = api.get("/api/products", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h02_nok_0008(api):
    resp = api.get("/api/products", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h02_nzd_0009(api):
    resp = api.get("/api/products", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h02_php_0010(api):
    resp = api.get("/api/products", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h02_pln_0011(api):
    resp = api.get("/api/products", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h02_ron_0012(api):
    resp = api.get("/api/products", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RON"


def test_h02_rub_0013(api):
    resp = api.get("/api/products", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h02_sek_0014(api):
    resp = api.get("/api/products", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h02_sgd_0015(api):
    resp = api.get("/api/products", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h02_thb_0016(api):
    resp = api.get("/api/products", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "THB"


def test_h02_try_0017(api):
    resp = api.get("/api/products", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h02_usd_0018(api):
    resp = api.get("/api/products", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "USD"


def test_h02_zar_0019(api):
    resp = api.get("/api/products", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h02_aud_0020(api):
    resp = api.get("/api/products", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h02_bgn_0021(api):
    resp = api.get("/api/products", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h02_brl_0022(api):
    resp = api.get("/api/products", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h02_cad_0023(api):
    resp = api.get("/api/products", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h02_chf_0024(api):
    resp = api.get("/api/products", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h02_cny_0025(api):
    resp = api.get("/api/products", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h02_czk_0026(api):
    resp = api.get("/api/products", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h02_dkk_0027(api):
    resp = api.get("/api/products", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h02_eur_0028(api):
    resp = api.get("/api/products", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h02_gbp_0029(api):
    resp = api.get("/api/products", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h02_hkd_0030(api):
    resp = api.get("/api/products", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h02_hrk_0031(api):
    resp = api.get("/api/products", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h02_huf_0032(api):
    resp = api.get("/api/products", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h02_idr_0033(api):
    resp = api.get("/api/products", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "IDR"
