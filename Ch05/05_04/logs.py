"""SQL example"""

import sqlite3
from random import choice
from datetime import datetime, timedelta

# use :memory: for in memory database, great for testing
db = sqlite3.connect('logs.db')

# Create the table
with open('schema.sql') as fp:
    schema_sql = fp.read()
db.executescript(schema_sql)
db.commit()


# Generate some random data
cur = db.cursor()  # Database cursor
now = datetime.now()
insert_sql = 'INSERT INTO logs (time, level, message) values (?, ?, ?)'
for i in range(10_000):
    time = now - timedelta(seconds=i)
    level = choice(['INFO', 'WRANING', 'ERROR'])
    message = f'log message #{i}'
    cur.execute(insert_sql, (time, level, message))
db.commit()


# Query the database
db.row_factory = sqlite3.Row  # Access column by name
cur = db.cursor()
query_sql = 'SELECT * FROM logs WHERE level = "INFO" LIMIT 5'
for row in cur.execute(query_sql):
    print(dict(row))
