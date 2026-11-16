import json  # noqa: F401


def test_h15_binoculars_0001(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0002(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0003(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0004(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0005(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0006(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0007(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0008(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0009(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0010(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0011(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0012(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0013(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0014(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0015(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]
