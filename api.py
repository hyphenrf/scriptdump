#!/usr/bin/env python3

from requests import post,get # interacts with APIs
# from pprint import pprint # pretty-print sometimes is useful for 
                            # prettifying json formatted one-liners
                            # see also: 
                            # python -c 'import pprint; help(pprint)'



req = get("https://some.api.url/option")

# with open('new.json','bw') as a:
#     a.write(bytes(req.content))

# print(req.content.decode()) # or:
print(req.text)

dataDict = req.json() # json is a method that returns a python doc
print(dataDict['title'])

