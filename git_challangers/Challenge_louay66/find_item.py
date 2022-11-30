#!/usr/bin/python3


import json
from operator import itemgetter
from .search import *


def filter_store(filename):
    """ filiter prodact in 6 file each store in file """

    with open(filename, 'r') as d:
        data = json.load(d)
        loblaws = []
        TNT = []
        saveonfoods = []
        wallmart = []
        nofrills = []
        realcanadiansuperstore = []
        
        for i in data:
            if i['store'] == 'loblaws':
               loblaws.append(i)
            if i['store'] == 'TNT':
               TNT.append(i)
            if i['store'] == 'saveonfoods':
               saveonfoods.append(i)
            if i['store'] == 'wallmart':
               wallmart.append(i)
            if i['store'] == 'nofrills':
               nofrills.append(i)
            if i['store'] == 'realcanadiansuperstore':
               realcanadiansuperstore.append(i)
        
    with open('loblaws.json', 'w') as to:
        newlist = sorted(loblaws, key=itemgetter('code')) 
        json.dump(newlist, to)
    with open('TNT.json', 'w') as to:
        newlist = sorted(TNT, key=itemgetter('id'))
        json.dump(newlist, to)
    with open('saveonfoods.json', 'w') as to:
        newlist = sorted(saveonfoods, key=itemgetter('code')) 
        json.dump(newlist, to)
    with open('wallmart.json', 'w') as to:
        newlist = sorted(wallmart, key=itemgetter('code'))
        json.dump(newlist, to)
    with open('nofrills.json', 'w') as to:
        newlist = sorted(nofrills, key=itemgetter('code'))
        json.dump(newlist, to)
    with open('realcanadiansuperstore.json', 'w') as to:
        newlist = sorted(realcanadiansuperstore, key=itemgetter('code'))
        json.dump(newlist, to)

    
if __name__ == "__main__":
    
    # this function  we have to call it once to parse the data and then we can comment it out
     filename = 'parsed_data.json'
     filter_store(filename)
     
     # put code or id in variable code and run program 
     code = "SP664104"
     print(find_item_list(code))