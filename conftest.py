import os
import uuid

import pytest
import requests

BASE_URL = os.environ.get("OTEL_DEMO_URL", "http://localhost:8080").rstrip("/")


class Api:
    """Calls the OpenTelemetry demo frontend API at BASE_URL."""

    def __init__(self):
        self.session = requests.Session()

    def request(self, method, path, **kwargs):
        kwargs.setdefault("timeout", 30)
        return self.session.request(method, BASE_URL + path, **kwargs)

    def get(self, path, **kwargs):
        return self.request("GET", path, **kwargs)

    def post(self, path, **kwargs):
        return self.request("POST", path, **kwargs)

    def delete(self, path, **kwargs):
        return self.request("DELETE", path, **kwargs)


@pytest.fixture(scope="session")
def api():
    return Api()


@pytest.fixture
def user_id(request):
    """A user ID no other test or earlier run uses, so carts never carry over."""
    return f"{request.node.name}-{uuid.uuid4().hex[:8]}"
