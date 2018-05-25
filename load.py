#!/usr/bin/python3
import cgi
import sys
import re


def success(lines):
    print('Content-Type: application/json')
    print('Cache-Control: private, no-store, no-cache, must-revalidate')
    print('Pragma: no-cache')
    print('')
    for line in lines:
        print(line)


def fail(message):
    print('Status: 400')
    print('Content-Type: application/json')
    print('')
    print('{{"error": "{}"}}'.format(message))


def read_data(name):
    filename = 'recording/{}'.format(name)
    with open(filename, 'r') as f:
        return f.readlines()

#
# main script
#
try:
    form = cgi.FieldStorage()

    name = form.getfirst('name')

    if name:
        name = re.sub('[^a-zA-Z_-]', '', name)
        lines = read_data(name)
        success(lines)
    else:
        fail('missing parameters')
except:
    fail(sys.exc_info()[0])

