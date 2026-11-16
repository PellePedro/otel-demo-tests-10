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


def test_h15_binoculars_0016(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0017(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0018(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0019(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0020(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0021(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0022(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0023(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0024(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0025(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0026(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0027(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0028(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0029(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0030(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0031(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0032(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0033(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0034(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0035(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0036(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0037(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0038(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0039(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0040(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0041(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0042(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0043(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0044(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0045(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0046(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0047(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0048(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0049(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0050(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0051(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0052(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0053(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0054(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0055(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0056(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0057(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0058(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0059(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0060(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0061(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0062(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0063(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0064(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0065(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0066(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0067(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0068(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0069(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0070(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0071(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0072(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0073(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0074(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0075(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0076(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0077(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0078(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0079(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0080(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0081(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0082(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0083(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0084(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0085(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0086(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0087(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0088(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0089(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0090(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0091(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0092(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0093(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0094(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0095(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0096(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0097(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0098(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0099(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0100(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0101(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0102(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0103(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0104(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0105(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0106(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0107(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0108(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0109(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0110(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0111(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0112(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0113(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0114(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0115(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0116(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0117(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0118(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0119(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0120(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0121(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0122(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0123(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0124(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0125(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0126(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0127(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0128(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0129(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0130(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0131(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0132(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0133(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0134(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0135(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0136(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0137(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0138(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0139(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0140(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0141(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0142(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0143(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0144(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0145(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0146(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0147(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0148(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0149(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0150(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0151(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0152(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0153(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0154(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0155(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0156(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0157(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0158(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0159(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0160(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0161(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0162(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0163(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0164(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0165(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0166(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0167(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0168(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0169(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0170(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0171(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0172(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0173(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0174(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0175(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0176(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0177(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0178(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0179(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0180(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0181(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0182(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0183(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0184(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0185(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0186(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0187(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0188(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0189(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0190(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0191(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0192(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0193(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0194(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0195(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0196(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0197(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0198(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0199(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0200(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0201(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0202(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0203(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0204(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0205(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0206(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0207(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0208(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0209(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0210(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0211(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0212(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0213(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0214(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0215(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0216(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0217(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0218(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0219(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0220(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0221(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0222(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0223(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0224(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0225(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0226(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0227(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0228(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0229(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0230(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0231(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0232(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0233(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0234(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0235(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0236(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0237(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0238(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0239(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0240(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0241(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0242(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0243(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0244(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0245(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0246(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0247(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0248(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0249(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0250(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0251(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0252(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0253(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0254(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0255(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0256(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0257(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0258(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0259(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0260(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0261(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0262(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0263(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0264(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0265(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0266(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0267(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0268(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0269(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0270(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0271(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0272(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0273(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0274(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0275(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0276(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0277(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0278(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0279(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0280(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0281(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0282(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0283(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0284(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0285(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0286(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0287(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0288(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0289(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0290(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0291(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0292(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0293(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0294(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0295(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0296(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0297(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0298(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0299(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0300(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0301(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0302(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0303(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0304(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0305(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0306(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0307(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0308(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0309(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0310(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0311(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0312(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0313(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0314(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0315(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0316(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0317(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0318(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0319(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0320(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0321(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0322(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0323(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0324(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0325(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0326(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0327(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0328(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0329(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0330(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0331(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0332(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0333(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0334(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0335(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0336(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0337(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0338(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0339(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0340(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0341(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0342(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0343(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0344(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0345(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0346(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0347(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0348(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0349(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0350(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0351(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0352(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0353(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0354(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0355(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_binoculars_0356(api):
    resp = api.get("/api/data", params={"contextKeys": ["binoculars"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_telescopes_0357(api):
    resp = api.get("/api/data", params={"contextKeys": ["telescopes"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_accessories_0358(api):
    resp = api.get("/api/data", params={"contextKeys": ["accessories"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 3
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_assembly_0359(api):
    resp = api.get("/api/data", params={"contextKeys": ["assembly"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]


def test_h15_travel_0360(api):
    resp = api.get("/api/data", params={"contextKeys": ["travel"]})
    assert resp.status_code == 200
    ads = resp.json()
    assert len(ads) == 1
    for ad in ads:
        assert ad["text"]
        assert ad["redirectUrl"]
