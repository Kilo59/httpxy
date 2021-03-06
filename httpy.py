"""
httpy
~~~~~
httpx with native yaml support.
"""

from typing import Any, Dict, Union

from httpx import *
from yaml import dump, load, safe_load

try:
    from yaml import CDumper as Dumper
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Dumper, Loader

CONTENT_TYPE = "Content-Type"
ACCEPT = "Accept"
YAML_TYPE = "application/yaml"


def _yaml(self, **load_kwargs: Any) -> Any:
    """Deserialize the content using `PyYaml` `safe_load()`."""
    return safe_load(self.content, **load_kwargs)


def dump_yaml(content: bytes) -> str:
    return dump(content, Dumper=Dumper)


setattr(Response, "yaml", _yaml)

if __name__ == "__main__":
    pass
