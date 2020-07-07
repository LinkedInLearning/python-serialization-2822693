"""Example serializing custom types"""
from datetime import datetime


def default(obj):
    """Encode datetime to string in YYYY-MM-DDTHH:MM:SS format (RFC3339)"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    return obj


def pairs_hook(pairs):
    """Convert the "time" key to datetime"""
    obj = {}
    for key, value in pairs:
        if key == 'time':
            value = datetime.fromisoformat(value)  # Python >= 3.7
        obj[key] = value
    return obj
