#!/usr/bin/python3


import json
from operator import itemgetter
from .Thread import ThreadWithResult

def search_loblaws(code : str):
    # to search into loblaws.json
    loblaws_same = []
    with open('git_challangers/Challenge_louay66/loblaws.json', 'r') as lobl :
        data = json.load(lobl)
        for i in range(0, len(data)):
            if data[i]['code'] == code:
                loblaws_same.append(data[i])
                k = i + 1
                for j in range(k, len(data)):
                
                    if data[j]['code'] == code:
                         loblaws_same.append(data[j])
                    else: 
                        break
                break
    return loblaws_same
                    
def search_TNT(code):
    # to search into TNT.json
    if code.isnumeric():
        code_int = int(code)
        TNT_same = []
        with open('TNT.json', 'r') as lobl :
            data = json.load(lobl)
            for i in range(0, len(data)):
                if data[i]['id'] == code_int:
                    TNT_same.append(data[i])
                    k = i + 1
                    for j in range(k, len(data)):
                
                        if data[j]['id'] == code_int:
                            TNT_same.append(data[j])
                        else: 
                            break
                    break
        return TNT_same
    else:
        return []

def search_saveonfoods(code : str):
    # to search into saveonfoods.json
    saveonfoods_same = []
    with open('git_challangers/Challenge_louay66/saveonfoods.json', 'r') as lobl :
        data = json.load(lobl)
        for i in range(0, len(data)):
            if data[i]['code'] == code:
                saveonfoods_same.append(data[i])
                k = i + 1
                for j in range(k, len(data)):
                
                    if data[j]['code'] == code:
                         saveonfoods_same.append(data[j])
                    else: 
                        break
                break
    return saveonfoods_same
def search_wallmart(code : str):
    # to search into wallmart.json
    wallmart_same = []
    with open('git_challangers/Challenge_louay66/wallmart.json', 'r') as lobl :
        data = json.load(lobl)
        for i in range(0, len(data)):
            if data[i]['code'] == code:
                wallmart_same.append(data[i])
                k = i + 1
                for j in range(k, len(data)):
                
                    if data[j]['code'] == code:
                         wallmart_same.append(data[j])
                    else: 
                        break
                break
    return wallmart_same

def search_nofrills(code : str):
    # to search into nofrills.json
    nofrills_same = []
    with open('git_challangers/Challenge_louay66/nofrills.json', 'r') as lobl :
        data = json.load(lobl)
        for i in range(0, len(data)):
            if data[i]['code'] == code:
                nofrills_same.append(data[i])
                k = i + 1
                for j in range(k, len(data)):
                
                    if data[j]['code'] == code:
                         nofrills_same.append(data[j])
                    else: 
                        break
                break
    return nofrills_same

def search_realcanadiansuperstore(code : str):
    # to search into realcanadiansuperstore.json
    realcanadiansuperstore_same = []
    with open('git_challangers/Challenge_louay66/realcanadiansuperstore.json', 'r') as lobl :
        data = json.load(lobl)
        for i in range(0, len(data)):
            if data[i]['code'] == code:
                realcanadiansuperstore_same.append(data[i])
                k = i + 1
                for j in range(k, len(data)):
                
                    if data[j]['code'] == code:
                         realcanadiansuperstore_same.append(data[j])
                    else: 
                        break
                break
    return realcanadiansuperstore_same

def find_item_list_l(item_id):
    # run 6 function search in same time and retunr list 
    

    a = ThreadWithResult(target=search_loblaws ,args= (item_id,))
    b =  ThreadWithResult(target=search_TNT , args= (item_id,))
    c =  ThreadWithResult(target=search_saveonfoods , args= (item_id,))
    d = ThreadWithResult(target=search_wallmart , args= (item_id,))
    e = ThreadWithResult(target=search_nofrills , args= (item_id,))
    f = ThreadWithResult(target=search_realcanadiansuperstore , args= (item_id,))
    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    loblaws = a.result
    TNT = b.result
    saveonfoods = c.result
    wallmart = d.result
    nofrills = e.result
    realcanadiansuperstore = f.result
    
    store = [loblaws, TNT, saveonfoods, nofrills, realcanadiansuperstore, wallmart]
    all_list = []
    
    for i in store:
        if i:
            for item in i:
                all_list.append(item)
        else:
            continue
    return all_list
   
       