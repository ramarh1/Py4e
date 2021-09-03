
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

count = 0
n = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
numbers = int(input('Enter count:'))
position = int(input('Enter position:'))

while n < numbers:    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')


# Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        count = count + 1
        if count == position:
         url  = tag.get('href', None)
         print("Retrieving:" , url)
         count = 0
         break
    n = n +1