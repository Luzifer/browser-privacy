import sys
import re
import codecs
import hashlib
import base64
import datetime

import pytz

checksumRegexp = re.compile(r'^! Checksum: ([\w\+\/=]+).*\n', re.M)
timeUpdRegexp = re.compile(r'^! TimeUpdated: (.*)\n', re.M)


def addChecksum(data):
    checksum = calculateChecksum(data)
    data = re.sub(checksumRegexp,
                  r'! Checksum: {}\n'.format(checksum),
                  data,
                  1)
    return data


def addDate(data):
    d = datetime.datetime.utcnow().replace(microsecond=0)
    d_with_timezone = d.replace(tzinfo=pytz.UTC)
    now = d_with_timezone.isoformat()

    return re.sub(timeUpdRegexp, r'! TimeUpdated: {}\n'.format(now), data)


def calculateChecksum(data):
    data = normalize(data)

    hash = hashlib.md5()
    hash.update(data.encode('utf-8'))
    return base64.b64encode(hash.digest()).decode('utf-8').rstrip('=')


def normalize(data):
    data = re.sub(r'\r', '', data)
    data = re.sub(r'\n+', '\n', data)
    data = re.sub(checksumRegexp, '', data)
    return data


if __name__ == '__main__':
    data = open('filters.txt').read()
    data = addDate(data)
    data = addChecksum(data)

    with open('filters.txt', 'w') as f:
        f.write(data)
