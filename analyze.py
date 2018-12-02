#!/usr/bin/env python3
import plistlib
from datetime import date
import os
from pprint import pprint
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

DATE = date.today().strftime('%Y-%m-%d')
DIR = '/Library/Application Support/JAMF/Usage/' + DATE + '/'
DIR = 'Usage/' + DATE + '/'
DIR = 'Usage/2018-12-01/'

users = os.listdir(DIR)
users = [user for user in users if user not in ['idle.plist']]
USERNAME = 'boesene'

with open(DIR + 'idle.plist', 'rb') as f:
    idle = plistlib.load(f, fmt=plistlib.FMT_XML)
with open(DIR + USERNAME + '.plist', 'rb') as f:
    user = plistlib.load(f, fmt=plistlib.FMT_XML)
"""with open(DIR + '(null).plist', 'rb') as f:
    null = plistlib.load(f, fmt=plistlib.FMT_XML)
pprint(null)"""

df = pd.DataFrame.from_dict(user, orient='index', columns=['name','foremost','open','secondsforemost','secondsopen','version'])
df.rename(columns={'': 'name'})
df.to_csv('data.csv')

#sns.barplot(col='name', y='secondsopen', data=df).figure.savefig('secondsopen.png')
print(df['name'])
plt.pie(df['secondsforemost'], labels=df['name'])
#fig1, ax1 = plt.subplots()
#ax1.pie(labels['secondsopen'], labels=tuple(df['name']), startangle=90)
#ax1.axis('equal')
plt.savefig('secondsopen.png')

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
