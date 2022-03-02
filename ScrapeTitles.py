
# coding: utf-8

# In[1]:

from lxml import html
import requests
import lxml.html
import requests

page = requests.get('https://www.goodreads.com/review/list/30013907-sami?ref=nav_mybooks&shelf=read')
tree = html.fromstring(page.content)


# In[2]:

tree = lxml.html.fromstring(page.text)
tbody_elem = tree.cssselect('tbody')[0]  # equivalent to previous XPath
print("tbody tag:", tbody_elem.tag)
#print("tbody text:", tbody_elem.text_content())
#print("tbody html:", lxml.html.tostring(tbody_elem))
print("tbody's childrens' tag:", tbody_elem.getchildren())
print(tbody_elem.getprevious())


# In[ ]:

children = tbody_elem.getchildren()
info = {}

for elem in children:
    info[elem] = elem.text_content()
len(info)


# In[ ]:

firstElem = list(info.keys())[0]
potato = info[firstElem]
import re
tags = re.sub("/ +/", " ",potato)
shortString = re.sub("\\n", " ", potato)
potato = shortString


# In[ ]:

parseElem = []
word = "empty"
i = 0
while (word != "\s+isbn"):
    tags = re.search("(\w+d*-*)",potato)
    #print(tags.group())
    word = "\s+" + tags.group()
    parseElem += word
    print(word)
    potato = re.sub(word, "", potato)
    i = i+1
parseElem


# In[ ]:



