"""ETL FROM UFO data in XML into SQLite database"""
import sqlite3
import xml.etree.ElementTree as xml
from datetime import datetime


insert_sql = 'INSERT INTO records VALUES (?, ?, ?, ?)'


def etl(xml_file, db_file):
    conn = sqlite3.connect(db_file)
    with open('schema.sql') as fp:
        schema_sql = fp.read()
    conn.executescript(schema_sql)

    root = xml.parse(xml_file).getroot()
    num_records = 0
    for elem in root.findall('.//sighting'):
        time = elem.find('time').text
        time = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S')
        lat = float(elem.find('lat').text)
        lng = float(elem.find('lng').text)
        shape = elem.find('shape').text
        conn.execute(insert_sql, (time, lat, lng, shape))
        num_records += 1

    return num_records


if __name__ == '__main__':
    count = etl('ufo.xml', 'ufo.db')
    print(f'{count} records loaded')
