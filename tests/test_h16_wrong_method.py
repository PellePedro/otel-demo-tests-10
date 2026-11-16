import json  # noqa: F401


def test_h16_put_api_currency_0001(api):
    resp = api.request("PUT", "/api/currency")
    assert resp.status_code == 405


def test_h16_post_api_currency_0002(api):
    resp = api.request("POST", "/api/currency")
    assert resp.status_code == 405


def test_h16_delete_api_currency_0003(api):
    resp = api.request("DELETE", "/api/currency")
    assert resp.status_code == 405


def test_h16_post_api_products_0004(api):
    resp = api.request("POST", "/api/products")
    assert resp.status_code == 405


def test_h16_delete_api_products_0005(api):
    resp = api.request("DELETE", "/api/products")
    assert resp.status_code == 405


def test_h16_put_api_products_oljcespc7z_0006(api):
    resp = api.request("PUT", "/api/products/OLJCESPC7Z")
    assert resp.status_code == 405


def test_h16_put_api_cart_0007(api):
    resp = api.request("PUT", "/api/cart")
    assert resp.status_code == 405


def test_h16_get_api_checkout_0008(api):
    resp = api.request("GET", "/api/checkout")
    assert resp.status_code == 405


def test_h16_post_api_shipping_0009(api):
    resp = api.request("POST", "/api/shipping")
    assert resp.status_code == 405


def test_h16_post_api_recommendations_0010(api):
    resp = api.request("POST", "/api/recommendations")
    assert resp.status_code == 405
