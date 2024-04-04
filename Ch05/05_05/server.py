import tomllib
from pprint import pprint

with open('config.toml', 'rb') as fp:
    config = tomllib.load(fp)

pprint(config, indent=4)
