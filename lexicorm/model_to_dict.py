from typing import Dict, List, Any

from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.inspection import inspect
from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy.orm.state import InstanceState


def model_to_dict(
        sqlalchemy_model: DeclarativeMeta,
        get_lazy: bool = False
) -> Dict[str, Any]:
    """
    sqlalchemy_model: A SQLAlchemy model
    :returns q dictionary representation of the SQLAlchemy Model

    """
    if sqlalchemy_model is None:
        return {}

    inspected = inspect(sqlalchemy_model)

    eager_relationships = _get_eager_relationships(inspected)
    lazy_relationships = _get_lazy_relationships(inspected)

    result: Dict[str, Any] = {
        **_model_to_dict(inspected,
                         lazy_keys=lazy_relationships,
                         get_lazy=get_lazy)
    }

    if eager_relationships:
        rels = _hydrate_eager_relationships(inspected, eager_relationships)
    else:
        rels = {}

    result.update(rels)

    return result


def _model_to_dict(
        inspected_sqlalchemy_model: InstanceState,
        lazy_keys: List[str],
        get_lazy: bool = False
) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    attrs = inspected_sqlalchemy_model.attrs
    for attr in attrs:
        if isinstance(attr.value, InstrumentedList):
            result[attr.key] = []
        elif attr.key in lazy_keys and get_lazy is False:
            continue
        else:
            result[attr.key] = attr.value
    return result


def _get_eager_relationships(
        inspected_sqlalchemy_model: InstanceState
) -> List[str]:
    return [
        model[1].key for model
        in inspected_sqlalchemy_model.mapper.relationships._data.items()
        if model[1].lazy is False
    ]


def _get_lazy_relationships(
        inspected_sqlalchemy_model: InstanceState
) -> List[str]:
    return [
        model[1].key for model
        in inspected_sqlalchemy_model.mapper.relationships._data.items()
        if model[1].lazy is True
    ]


def _convert_model_list_to_dicts(
        model_list: List[InstanceState]
) -> List[Dict[str, Any]]:
    return [model_to_dict(inspect(model)) for model in model_list]


def _hydrate_eager_relationships(
        inspected_sqlalchemy_model: InstanceState,
        eager_relationships: List[str]
) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    attrs = inspected_sqlalchemy_model.attrs
    for attr in attrs:
        if attr.key in eager_relationships:
            result[attr.key] = _convert_model_list_to_dicts(attr.value)
    return result
