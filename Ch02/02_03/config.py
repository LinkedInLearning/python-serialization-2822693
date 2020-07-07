"""Server configuration"""
import logging
import sys
from os import environ


api_key = environ.get('API_KEY') or 'test-api-key'
log_level = logging.INFO
port = 8080

if sys.platform == 'win32':
    num_workers = 10
else:
    num_workers = 100


# Clean up namespace
del __doc__
del environ
del logging
del sys
