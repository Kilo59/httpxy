"""
test.conftest.py
~~~~~~~~~~~~~~~~
Root conftest module.
"""
import contextlib
import logging

import httpx
import pytest
import respx
from pprintpp import pformat as pf

from httpxy import _dump_yaml, safe_load

from .data import ACCEPT, CONTENT_TYPE, YAML_TYPE

LOGGER = logging.getLogger("tests")

EXAMPLE_BASE_URL = "https://yaml.example"


def yaml_content_se(request: httpx.Request, **kwargs) -> httpx.Response:
    content_type = request.headers.get(CONTENT_TYPE)
    LOGGER.info(f"{request} - {CONTENT_TYPE}: {content_type}")

    if content_type == YAML_TYPE:
        yaml_data = safe_load(request.content)
        LOGGER.info(f"yaml: {pf(yaml_data, depth=2)}")
        return httpx.Response(200, content=_dump_yaml({"accepted": yaml_data}).encode())

    return httpx.Response(400, text="Not YAML")


def yaml_accept_se(request: httpx.Request, **kwargs) -> httpx.Response:
    accept = request.headers.get(ACCEPT)
    LOGGER.info(f"{request} - {ACCEPT}: {accept}")

    # TODO: finish
    return None


@contextlib.contextmanager
def yaml_api_mocker(base_url=EXAMPLE_BASE_URL, **mock_kwargs) -> respx.MockRouter:
    with respx.mock(base_url=base_url, **mock_kwargs) as respx_mock:

        send_yaml = respx_mock.route(method__in=["PUT", "PATCH", "POST"])
        send_yaml.mock(side_effect=yaml_content_se)

        accept_yaml = respx_mock.route(method="GET")
        accept_yaml.mock(side_effect=yaml_accept_se)

        yield respx


@pytest.fixture(scope="session", autouse=True)
def yaml_api_mock_session(autouse=True):
    with yaml_api_mocker(assert_all_called=False) as respx_mock:
        yield respx_mock


@pytest.fixture(scope="session")
def base_url() -> str:
    return EXAMPLE_BASE_URL
