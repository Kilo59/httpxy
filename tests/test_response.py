"""
tests.test_response.py
~~~~~~~~~~~~~~~~~~~~~~
"""
import pytest
import httpy
from yaml import YAMLObject

SIMPLE_LIST = """
- Hesperiidae
- Papilionidae
- Apatelodidae
- Epiplemidae
"""
SIMPLE_DICT = """
name: Silenthand Olleander
race: Human
traits: [ONE_HAND, ONE_EYE]
"""
ANY_TYPE = """
none: [~, null]
bool: [true, false, on, off]
int: 42
float: 3.14159
list: [LITE, RES_ACID, SUS_DEXT]
dict: {hp: 13, sp: 5}
"""
PY_OBJECT = """
!!python/object:__main__.Hero
name: Welthyr Syxgon
hp: 1200
sp: 0
"""


class Hero(YAMLObject):
    yaml_tag = "!Hero"

    def __init__(self, name, hp, sp):
        self.name = name
        self.hp = hp
        self.sp = sp

    def __repr__(self):
        return "%s(name=%r, hp=%r, sp=%r)" % (
            self.__class__.__name__,
            self.name,
            self.hp,
            self.sp,
        )


@pytest.mark.parametrize(
    "content, expected",
    [
        (
            SIMPLE_LIST.encode(),
            ["Hesperiidae", "Papilionidae", "Apatelodidae", "Epiplemidae"],
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
        (SIMPLE_DICT.encode(), Hero(name="Welthyr Syxgon", hp=1200, sp=0)),
        (
            PY_OBJECT.encode(),
            {
                "name": "Silenthand Olleander",
                "race": "Human",
                "traits": ["ONE_HAND", "ONE_EYE"],
            },
        ),
    ],
)
def test_yaml(content, expected):
    r = httpy.Response(200, content=content)
    assert expected == r.yaml()


if __name__ == "__main__":
    pytest.main(args=["-vv"])
