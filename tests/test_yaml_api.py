"""
tests.test_yaml_api.py
~~~~~~~~~~~~~~~~~~~~~~
"""
import pytest
from pprintpp import pformat as pf

import httpxy

from .data import ANY_TYPE, CONTENT_TYPE, SIMPLE_DICT, SIMPLE_LIST, YAML_TYPE


@pytest.mark.parametrize(
    "method, kwargs",
    [
        (httpxy.post, {"headers": {CONTENT_TYPE: YAML_TYPE}, "data": SIMPLE_LIST}),
        (httpxy.put, {"headers": {CONTENT_TYPE: YAML_TYPE}, "data": SIMPLE_DICT}),
        (httpxy.patch, {"headers": {CONTENT_TYPE: YAML_TYPE}, "data": ANY_TYPE}),
        # (httpxy.post, {"yaml": SIMPLE_LIST}),
        # (httpxy.put, {"yaml": SIMPLE_DICT}),
        # (httpxy.patch, {"yaml": ANY_TYPE}),
    ],
)
def test_send_methods(base_url, method, kwargs):
    print(f"{method.__name__}: {pf(kwargs)}\n")

    response = method(base_url, **kwargs)

    print(response)
    print(response.content)


if __name__ == "__main__":
    pytest.main(args=["-vv"])
