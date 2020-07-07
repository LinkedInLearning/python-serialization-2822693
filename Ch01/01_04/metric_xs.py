"""Generate metric in CSV & XML"""
import csv
import xml.etree.ElementTree as xml
from sys import stdout
from xml.dom import minidom  # Used for pretty printing

from metric import metric

print('CSV')
headers = ['time', 'name', 'value']
writer = csv.DictWriter(stdout, fieldnames=headers)
writer.writeheader()
row = {k: v for k, v in metric.items() if k in headers}
writer.writerow(row)


def element(tag, text):
    elem = xml.Element(tag)
    elem.text = text
    return elem


def pretty_print(elem):
    dom = minidom.parseString(xml.tostring(elem))
    print(dom.toprettyxml(indent='    '))


print('XML')
root = xml.Element('metric')
root.append(element('time', metric['time'].isoformat()))
root.append(element('name', metric['name']))
root.append(element('value', str(metric['value'])))
labels = xml.Element('labels')
for key, value in metric['labels'].items():
    labels.append(xml.Element('label', key=key, value=value))
root.append(labels)
pretty_print(root)
