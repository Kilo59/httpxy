# httpy
HTTP client with yaml support

Adds minor convenience features to the excellent [`httpx`](https://www.python-httpx.org/) library which aims to make working with `yaml` easier and safer.

## Installation

```
pip install httpy
```

## Features
* Always use `safe_load()`. `DONE`
* `Response` objects have a `response.yaml()` for deserializing YAML to a `dict`. `DONE`
* Automatic serialization of objects to yaml. `TODO`
* Automatic deserializing of yaml to python objects/classes/models. `TODO`
* Works with multiple yaml packages. `TODO`


## Examples

### Deserialize directly from `Response` objects.

Equivalent to `response.json()`.

```python
import httpy
from pprint import pprint

response = httpy.get("https://mockbin.org/request", headers={"accept": "application/yaml"})

dict_from_yaml = response.yaml()

pprint(dict_from_yaml, sort_dicts=False, depth=1)
```

```python
    {'startedDateTime': '2021-03-06T19:54:03.157Z',
     'clientIPAddress': '99.99.999.999',
     'method': 'GET',
     'url': 'https://mockbin.org/request',
     'httpVersion': 'HTTP/1.1',
     'cookies': None,
     'headers': {...},
     'queryString': {},
     'postData': {...},
     'headersSize': 559,
     'bodySize': 0}

```

```python
print(response.text)
```

```yaml
    startedDateTime: '2021-03-06T19:54:03.157Z'
    clientIPAddress: 99.99.999.999
    method: GET
    url: 'https://mockbin.org/request'
    httpVersion: HTTP/1.1
    cookies:
    headers:
      host: mockbin.org
      connection: close
      accept-encoding: gzip
      x-forwarded-proto: http
      cf-visitor: '{"scheme":"https"}'
      accept: application/yaml
      user-agent: python-httpx/0.17.0
    queryString: {}
    postData:
      mimeType: application/octet-stream
      text: ""
      params: []
    headersSize: 559
    bodySize: 0
```
