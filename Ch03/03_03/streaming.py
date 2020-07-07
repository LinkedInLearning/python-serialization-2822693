"""Example of streaming JSON"""

import json
from io import BytesIO

groups = [
    {'animal': 'bee', 'group': 'swarm'},
    {'animal': 'fox', 'group': 'charm'},
    {'animal': 'whale', 'group': 'pod'},
]


# Sending side
network = BytesIO()
for message in groups:
    data = json.dumps(message)
    network.write(data.encode('utf-8'))  # Sockets work in byte level
    network.write(b'\n')


# Receiving side
network.seek(0)  # Go back to start of data for reading side

while True:
    line = network.readline()
    if not line:
        break

    message = json.loads(line)
    print('got', message)
