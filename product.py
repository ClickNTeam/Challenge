#!/usr/bin/python3
from typing import Text
from redis_om import Field, HashModel, JsonModel
from redisearch.client import TagField
from redis_om import get_redis_connection

redis = get_redis_connection(host='',
                             port=18717,
                             password='',
                             decode_responses=True
                             )

class Product(JsonModel):
    code: str = Field(index=False)
    store: str = Field(index=True)
    category: str = Field(index=True, full_text_search=True)
    brand: str = Field(index=True, full_text_search=True)
    name: str = Field(index=True, full_text_search=True)
    description: str = Field(index=False, full_text_search=True)
    image: str = Field(index=False)
    measurement: str = Field(index=False)
    price: float = Field(index=False)
    price_type: str = Field(index=False)
    instock: str = Field(index=False)
    
    class Meta():
        database = redis

x = {
        "code": "20135384_EA",
        "store": "loblaws",
        "category": "Dairy & Eggs, Milk",
        "brand": "Neilson",
        "name": "Buttermilk",
        "description": "Buttermilk can be drank straight but is often used in cooking and baking. It is thicker than plain milk and has a characteristically sour taste.",
        "image": "https://assets.shop.loblaws.ca/products/20135384/b1/en/front/20135384_front_a01_@2.png",
        "measurement": "1 l",
        "price": 4.39,
        "price_type": "SOLD_BY_EACH",
        "inStock": "LOW"
    }
p = Product(**x)
p.save()
