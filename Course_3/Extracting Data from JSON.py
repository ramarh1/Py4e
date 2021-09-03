
import json
import urllib.parse
import urllib.request
total = 0



address = input('Enter location: ')

if len(address) < 1: 
    address = ''
    
print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read()

print('Retrieved', len(data), 'characters')


info = json.loads(data)
print('Count:', len(info['comments']))
    
for item in info['comments']:

    item = (item['count'])
    item = int(item)
    total = item + total

print('Sum:', total)








