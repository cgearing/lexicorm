from typing import Dict

from sqlalchemy.ext.declarative import DeclarativeMeta


def model_to_dict(sqlalchemy_model: DeclarativeMeta) -> Dict:
    if sqlalchemy_model is None:
        return {}
