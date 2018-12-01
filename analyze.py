#!/usr/bin/env python3
import plistlib
from datetime import date
import os
from pprint import pprint

DATE = date.today().strftime('%Y-%m-%d')
DIR = '/Library/Application Support/JAMF/Usage/' + DATE + '/'
DIR = 'Usage/' + DATE + '/'

users = os.listdir(DIR)
users = [user for user in users if user not in ['idle.plist']]
USERNAME = 'boesene'

with open(DIR + 'idle.plist', 'rb') as f:
    idle = plistlib.load(f, fmt=plistlib.FMT_XML)
pprint(idle)
with open(DIR + USERNAME + '.plist', 'rb') as f:
    user = plistlib.load(f, fmt=plistlib.FMT_XML)
pprint(user)
with open(DIR + '(null).plist', 'rb') as f:
    null = plistlib.load(f, fmt=plistlib.FMT_XML)
pprint(null)

"""
for user in users:
    # Usage logs are technically plist files, but are in XML format.
    tree = xml.etree.ElementTree.parse(DIR + user)
    main = tree.getroot().find('dict')
    # Change app headers to something random
    for key in main.findall('key'):
        key.text = ''
    for entry in main.findall('dict'):
        for field in entry.findall('string'):
            field.text = 3
            """
