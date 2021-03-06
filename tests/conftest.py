"""
test.conftest.py
~~~~~~~~~~~~~~~~
Root conftest module.
"""
import contextlib

import pytest
import respx

EXAMPLE_BASE_URL = "https://yaml.example"


@contextlib.contextmanager
def yaml_api_mocker(base_url=EXAMPLE_BASE_URL, **mock_kwargs) -> respx.MockRouter:
    with respx.mock(base_url=base_url, **mock_kwargs) as respx_mock:
        # TODO: check content-types
        yield respx


@pytest.fixture(scope="session")
def yaml_api_mock_session(autouse=True):
    with yaml_api_mocker() as respx_mock:
        yield respx_mock
