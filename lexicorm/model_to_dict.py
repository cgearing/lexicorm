from typing import Dict

from sqlalchemy.ext.declarative import DeclarativeMeta


def model_to_dict(sqlalchemy_model: DeclarativeMeta) -> Dict:
    """
    sqlalchemy_model: A SQLAlchemy model
    :returns An dictionary representation of the SQLAlchemy Model

    """
    if sqlalchemy_model is None:
        return {}
    return sqlalchemy_model.__dict__
