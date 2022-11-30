# api
import json
from rapidfuzz import fuzz
import re
from fastapi import FastAPI
from git_challangers.Challenge_cryptolake.itemsgraph import ItemsGraph

app = FastAPI()


def preprocess(data):
    """Preprocess Data."""
    proc_data = {}
    for i, x in enumerate(data):
        brand = re.sub(r'[^\w]', ' ', x.get('brand', '')).strip()
        name = re.sub(r'[^\w]', ' ', x.get('name', '')).strip()
        brand = brand.lower()
        name = name.lower()
        name = name.replace(brand, '')
        x.update({'code': x.get('code'), 'name': name,
                  'brand': brand, 'price': x.get('price')})
        proc_data[str(i)] = x
    return proc_data


with open('git_challangers/Challenge_cryptolake/parsed_data.json', 'r') as f:
    data = json.load(f)

# preprocess data: make the data into ids because there are no reliable field to use
# as id.
data = preprocess(data)
# initialize the graph with a a list of fields to compare and minimum
# percentages a function to compare string and the degree of tolerance
# of price filtering.
graph = ItemsGraph(data, ['name', 'brand'], [50, 70],
                   fuzz.ratio, 0.2)
# graph.load('./items_graph.json')


@app.get("/")
async def root():
    return {"message": "Hello!"}


@app.get("/graph/load/{path}")
async def load_graph(path):
    graph.load(path)
    return {'message': "Graph Loaded!"}


@app.get("/graph/search/{id}")
async def search_graph(id):
    q, r = graph.search(str(id))
    return {"Query data": q, "Similar items": r}


@app.get("/graph/build")
async def build_graph():
    graph.build()
    return {"message": "Building Done"}


@app.get("/data/get/{id}")
async def get_data(id):
    return {str(id): graph.get(id)}


@app.get("/graph/save/{path}")
async def save_graph(path):
    graph.save(path, 2)
    return {'message': "Graph Saved"}
