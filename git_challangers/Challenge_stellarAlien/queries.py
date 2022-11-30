#!/usr/bin/env python3
"""
using redis search here
"""
import redis
from redisearch import Client, IndexDefinition, TextField, NumericField, TagField, GeoField, Query
from product import Product
from typing import Optional
from redisearch.aggregation import AggregateRequest, Asc, Desc
from redisearch import reducers

# check ressearch is installed
# set this to prodct jsonmodel
def initializeClient():
    SCHEMA = (
        TextField("code"),
        TextField("store"),
        TextField("category"),
        TextField("brand"),
        TextField('name'),
        TextField("description"),
        TextField("image"), # check if optimal to store a link 
        TextField("measurement"),
        NumericField("price"),
        TextField("price_type"),
    )
    client = Client("myIndex")
    definition = IndexDefinition(prefix=[':employee.Employee:'])
    try:
        client.info()
    except redis.ResponseError:
        # Index does not exist. We need to create it!
        client.create_index(SCHEMA, definition=definition)
    return client
client = initializeClient()

# todo 1: query by code/brand
def search_by_name(ft):
    """"""
    name="Buttermilk"
    r = ft.search(f"@name:Buttermilk")
    # the title has been indexed as text, so the field is tokenized and stemmed
    for i in r.docs:
        print(i)
        
# def search_by_name_faster
def search_by_name_fast(ft, name: Optional[str] = ""):
    """use verbatim to desactivate stemming and fuzzy search"""
    q = Query("").verbatim().paging() #.slop().language(langauge=ES).highlight(fields=[], tags=[])
    
# todo2 search by wildcard
def fuzzy_search(ft):
    """Fuzzy matches are performed based on Levenshtein distance (LD)."""
    r = ft.search("@description: *Milk*")
    if not r:
        r = ft.search("@description: '%'Milk%")
    for i in r.docs:
        print(i)
    
    
# todo3: query by description
def search_by_description(ft):
    """"""
    r = ft.search("@description: drank straight")
    for i in r.docs:
        print(i)
        
# todo4 query by name and description
def search_by_name_description(ft, description:Optional[str] = "",
                               name:Optional[str] = ""):
    """"""
    r = ft.search("@description: {description} @name: {name}")
    for i in r.docs:
        print(i)

# query_by_price
def search_by_price(ft, min: Optional[float] = 1, max: Optional[float] = float('inf')):
    """search by price in certain range"""
    r = ft.search(f"@price: [{min} {max}]")
    for i in r.docs:
        print(i)

def search_cheap(ft, max: Optional[float] = 50.00, category: str = 'Milk'):
    """"""
    # use verbatim to desactivate stemming and fuzzy search
    q = AggregateRequest(['name', 'category']).group_by(["@price"]).filter(f"@price: <{max}")
    r = ft.aggregate(q)
    for i in r.rows:
        print(i)
