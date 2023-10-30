# Imports
import pytest
from starlette.testclient import TestClient


# Local imports
from app.main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here
