import sys
import re
import codecs
import hashlib
import base64

checksumRegexp = re.compile(
    r'^\s*!\s*checksum[\s\-:]+([\w\+\/=]+).*\n', re.I | re.M)


def addChecksum(data):
    checksum = calculateChecksum(data)
    data = re.sub(checksumRegexp, '', data)
    data = re.sub(r'(\r?\n)', r'\1! Checksum: %s\1' % checksum, data, 1)
    return data


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
    data = addChecksum(open('filters.txt').read())
    with open('filters.txt', 'w') as f:
        f.write(data)
