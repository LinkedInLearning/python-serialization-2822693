"""Basic usage of JSON"""
import json

from event import event

# Serialize to bytes, dict keys must be str
data = json.dumps(event)
print('serialized:', data)
print('data type:', type(data))
data_bytes = data.encode('utf-8')
print('data_bytes type:', type(data_bytes))

# Indent
print('serialized indented:', json.dumps(event, indent=4))

event_str = json.loads(data)
print('equal:', event_str == event)

event_bytes = json.loads(data_bytes)  # Can loads from bytes as well
print('equal (bytes):', event_bytes == event)

# Working with files
with open('event.json', 'w') as out:
    json.dump(event, out)

with open('event.json') as fp:
    event_file = json.load(fp)

print('equal (file):', event_file == event)
