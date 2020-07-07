"""Generate metric in YAML & TOML"""
import toml
import yaml

from metric import metric

print('YAML')
print(yaml.dump(metric, default_flow_style=False, sort_keys=False))

print('\nTOML')
print(toml.dumps(metric))
