
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
total = 0

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
  
   # print('Contents:', tag.contents[0])
    contents = int(tag.contents[0])

    count = count + 1
    total = total + contents

print('Count', count)
print('Sum', total)