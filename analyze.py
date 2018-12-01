#!/usr/bin/env python3
import xml.etree.ElementTree
from datetime import date
import os

DATE = date.today().strftime('%Y-%m-%d')
DIR = '/Library/Application Support/JAMF/Usage/' + DATE + '/'
DIR = 'Usage/' + DATE + '/'

users = os.listdir(DIR)
users = [user for user in users if user not in ['idle.plist']]

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
