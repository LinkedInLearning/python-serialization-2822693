"""ETL FROM UFO data in XML into SQLite database"""
import sqlite3
import xml.etree.ElementTree as xml


def etl(xml_file, db_file):
    num_records = 0

    # Your code goes here

    return num_records


if __name__ == '__main__':
    count = etl('ufo.xml', 'ufo.db')
    print(f'{count} records loaded')
