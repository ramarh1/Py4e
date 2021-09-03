import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

while True:
    address = input('Enter location: ')
    if len(address) < 1: 
        address = 'http://py4e-data.dr-chuck.net/comments_1233510.xml'

    print('Retrieving', address)
    uh = urllib.request.urlopen(address)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)
    
    total = 0
    counts = tree.findall('.//count')
    for item in counts:

        item = int(item.text)

        total = item + total

    print('Count:',str(len(counts)))
    print('Sum:',total)