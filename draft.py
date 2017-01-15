#! /usr/bin/python

import uuid
import urllib
import time

fd = open('queue.txt', 'r')
next_url = 'http://www.anandtech.com\n'
res = open('results.txt', 'w')

print 'starting'
while next_url:
    next_url = fd.readline().strip()
    if not next_url:
        break
    print next_url
    url_uuid = str(uuid.uuid4())
    print '  ' + url_uuid
    fetch_res = urllib.urlretrieve(next_url, '/'.join(['data',url_uuid]))
    res.write(', '.join([next_url, str(time.time()), url_uuid]) + '\n')
