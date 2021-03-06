"""
tests.test_response.py
~~~~~~~~~~~~~~~~~~~~~~
"""
import pytest

import httpy

from .data import ANY_TYPE, PY_OBJECT, SIMPLE_DICT, SIMPLE_LIST, Hero


@pytest.mark.parametrize(
    "content, expected",
    [
        (
            SIMPLE_LIST.encode(),
            ["Hesperiidae", "Papilionidae", "Apatelodidae", "Epiplemidae"],
        ),
        (
            SIMPLE_DICT.encode(),
            {
                "name": "Silenthand Olleander",
                "race": "Human",
                "traits": ["ONE_HAND", "ONE_EYE"],
            },
        ),
        (
            ANY_TYPE.encode(),
            {
                "none": [None, None],
                "int": 42,
                "float": 3.1415899999999999,
                "list": ["LITE", "RES_ACID", "SUS_DEXT"],
                "dict": {"hp": 13, "sp": 5},
                "bool": [True, False, True, False],
            },
        ),
        # (PY_OBJECT.encode(), Hero(name="Welthyr Syxgon", hp=1200, sp=0)),
    ],
)
def test_yaml(content, expected):
    r = httpy.Response(200, content=content)
    assert expected == r.yaml()


if __name__ == "__main__":
    pytest.main(args=["-vv"])
