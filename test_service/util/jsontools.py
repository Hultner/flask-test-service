"""Collection of tools making JSON-handling easier.
"""
import json
from datetime import datetime
from sqlalchemy.ext.declarative import DeclarativeMeta


class ExtendedEncoder(json.JSONEncoder):
    """Extended JSONEncoder with support for datetime and SQLAlchemy objects.
    """
    def default(self, o):  # pylint: disable=E0202
        # o is used to support kwargs as default JSONEncoder uses o
        # E0202 is a false positive https://github.com/PyCQA/pylint/issues/414
        if isinstance(o.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            # return a json-encodable dict
            return o.as_dict()

        if isinstance(o, datetime):
            # a datetime object
            # return datetime ISO-string
            return o.isoformat()

        return json.JSONEncoder.default(self, o)


def json_dump(obj):
    """Shorthand for dumping json with the ExtendedEncoder.
    Args:
        obj: Serializable object to be JSONEncoded.
    """
    return json.dumps(obj, cls=ExtendedEncoder)
