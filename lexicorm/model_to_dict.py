from typing import Dict

from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.inspection import inspect
from sqlalchemy.orm.collections import InstrumentedList


def model_to_dict(sqlalchemy_model: DeclarativeMeta) -> Dict:
    """
    sqlalchemy_model: A SQLAlchemy model
    :returns q dictionary representation of the SQLAlchemy Model

    """
    if sqlalchemy_model is None:
        return {}

    result = {}

    attrs = inspect(sqlalchemy_model).attrs

    for attr in attrs:
        if type(attr.value) == InstrumentedList:
            result[attr.key] = []
        else:
            result[attr.key] = attr.value

    return result
