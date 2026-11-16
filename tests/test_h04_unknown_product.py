import json  # noqa: F401


def test_h04_unknown0000_0001(api):
    resp = api.get("/api/products/UNKNOWN0000")
    assert resp.status_code >= 400


def test_h04_unknown0001_0002(api):
    resp = api.get("/api/products/UNKNOWN0001")
    assert resp.status_code >= 400


def test_h04_unknown0002_0003(api):
    resp = api.get("/api/products/UNKNOWN0002")
    assert resp.status_code >= 400


def test_h04_unknown0003_0004(api):
    resp = api.get("/api/products/UNKNOWN0003")
    assert resp.status_code >= 400


def test_h04_unknown0004_0005(api):
    resp = api.get("/api/products/UNKNOWN0004")
    assert resp.status_code >= 400
