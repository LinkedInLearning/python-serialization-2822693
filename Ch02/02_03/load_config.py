"""Load configuration with exec"""
from types import SimpleNamespace


def load_config(path):
    """"Load configuration from path"""
    with open(path) as fp:
        data = fp.read()

    ns = {}
    exec(data, {}, ns)
    return SimpleNamespace(**ns)
