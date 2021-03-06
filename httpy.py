"""
httpy
~~~~~
httpx with native yaml support.
"""

from httpx import *

from typing import Union, Dict, Any

from yaml import load, dump, safe_load

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def _yaml(self, **load_kwargs: Any) -> Any:
    """Deserialize the content using `PyYaml` `safe_load()`."""
    return safe_load(self.content, **load_kwargs)


def dump_yaml(content: bytes) -> str:
    return dump(content, Dumper=Dumper)


setattr(Response, "yaml", _yaml)

if __name__ == "__main__":
    pass
