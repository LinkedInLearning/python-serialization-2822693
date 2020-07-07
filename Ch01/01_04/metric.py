"""Metric data"""
from datetime import datetime

metric = {
    'time': datetime.now(),
    'name': 'memory',
    'value': 14.3,
    'labels': {
        'host': 'prod7',
        'version': '1.3.4',
    },
}
