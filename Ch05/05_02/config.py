"""Working with YAML example"""
from sys import stdout

import yaml

# de-serialize
with open('config.yml') as fp:
    config = yaml.safe_load(fp)
print(config)

# serialize
yaml.safe_dump(config, stdout)
