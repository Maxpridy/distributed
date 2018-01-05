
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://tools.ietf.org/html/rfc2616"
html = urlopen(url).read()
soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

with open('output_htmlrfc.txt','w',encoding='utf-8') as f:
    f.write(text)
    f.close()
