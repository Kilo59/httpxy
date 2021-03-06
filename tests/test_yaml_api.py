"""
tests.test_yaml_api.py
~~~~~~~~~~~~~~~~~~~~~~
"""
import pytest
from pprintpp import pformat as pf

import httpy
from httpy import CONTENT_TYPE, YAML_TYPE

from .data import ANY_TYPE, SIMPLE_DICT, SIMPLE_LIST


@pytest.mark.parametrize(
    "method, kwargs",
    [
        (httpy.post, {"headers": {CONTENT_TYPE: YAML_TYPE}, "data": SIMPLE_LIST}),
        (httpy.put, {"headers": {CONTENT_TYPE: YAML_TYPE}, "data": SIMPLE_DICT}),
        (httpy.patch, {"headers": {CONTENT_TYPE: YAML_TYPE}, "data": ANY_TYPE}),
        # (httpy.post, {"yaml": SIMPLE_LIST}),
        # (httpy.put, {"yaml": SIMPLE_DICT}),
        # (httpy.patch, {"yaml": ANY_TYPE}),
    ],
)
def test_send_methods(base_url, method, kwargs):
    print(f"{method.__name__}: {pf(kwargs)}\n")

    response = method(base_url, **kwargs)

    print(response)
    print(response.content)


if __name__ == "__main__":
    pytest.main(args=["-vv"])
