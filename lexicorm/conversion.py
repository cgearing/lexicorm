from typing import Mapping, Any

import inflection

from .type import JSONType


def python_dict_to_json_dict(
        input: Mapping[str, Any]
) -> Mapping[str, JSONType]:
    return {
        inflection.camelize(key, False): value for key, value in input.items()
    }


def json_dict_to_python_dict(
        input: Mapping[str, JSONType]
) -> Mapping[str, JSONType]:
    return {
        inflection.underscore(key): value for key, value in input.items()
    }
