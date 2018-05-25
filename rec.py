#!/usr/bin/python3
import cgi
import json
import sys
import re


def success(data):
    print('Content-Type: application/json')
    print('')
    print(json.dumps(data))


def fail(message):
    print('Status: 400')
    print('Content-Type: application/json')
    print('')
    print('{{"error": "{}"}}'.format(message))

def write_data(data):
    filename = 'recording/{}'.format(data['name'])
    with open(filename, 'w') as f:
        f.write(json.dumps(data))

#
# main script
#
try:
    form = cgi.FieldStorage()

    data = {}
    data['name'] = form.getfirst('name')
    data['lat'] = form.getfirst('lat')
    data['lon'] = form.getfirst('lon')
    data['time'] = form.getfirst('time')
    data['alt'] = form.getfirst('alt')
    data['speed'] = form.getfirst('speed')
    data['battery'] = form.getfirst('battery')

    if data['lat'] and data['lon'] and data['name']:
        data['name'] = re.sub('[^a-zA-Z_-]', '', data['name']) if data['name'] else None
        write_data(data)
        success(data)
    else:
        fail('missing parameters')
except:
    fail(sys.exc_info()[0])

