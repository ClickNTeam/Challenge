"""Implement graph as a recommendation engine for similar items."""
import json
from typing import Callable
from rapidfuzz import process


class ItemsGraph:
    """
    This is a class for all items.

    it is to be initialized with the dict of all items,
    it would return a graph data structure with every product and it's matches.
    """

    def __init__(self, data: dict, strs: list,
                 min_strs: list, filter_func: Callable, price_diff: float):
        """Initialize."""
        self.__data = data
        self.graph = {}
        self.strs = strs
        self.min_strs = min_strs
        self.filter_func = filter_func
        self.price_diff = price_diff
        self.data_size = len(data)
        self.__create_data(self.__data)

    def __create_data(self, data: dict):
        """Prepare additional Data."""
        flatten_dicts = {}
        for i in data:
            for k in data[i]:
                if flatten_dicts.get(k) is not None:
                    flatten_dicts[k][i] = data[i][k]
                else:
                    flatten_dicts[k] = {}
        self.__data_to_proc = list(data.keys())
        self.flatten_data = flatten_dicts

    def __filter_prices(self, price: float) -> list:
        """Filter data to price."""
        price_diff = price * self.price_diff
        filtered_prices = list(filter(lambda x: self.__data[x] if abs(self.__data[x]['price'] - price)
                                      <= price_diff else None,
                                      self.__data_to_proc))
        return filtered_prices

    def __filter_strings(self, i: str, data_ids: list) -> list:
        """Filter the strings."""
        for key, mm in zip(self.strs, self.min_strs):
            to_filter = {k: self.flatten_data[key].get(k) for k in data_ids}
            filtered = process.extract(self.__data[i][key], to_filter,
                                       scorer=self.filter_func, score_cutoff=mm)
            data_ids = [x[2] for x in filtered]

        return data_ids

    def __build_op(self, i: str, data: dict) -> dict:
        filter_prices = self.__filter_prices(data[i]['price'])
        filtered = self.__filter_strings(i, filter_prices)
        if i in filtered:
            filtered.remove(i)
        nodes = {i: filtered}
        for f in filtered:
            nodes[f] = list(filtered)
            nodes[f].append(i)
            nodes[f].remove(f)
            self.__data_to_proc.remove(f)
        return nodes

    def build(self, progress=True, prog_rate=1, to_build: list = []):
        """Build graph."""
        if len(to_build) != 0:
            self.__data_to_proc = to_build

        toggle = 0
        counter = 0
        for i in self.__data_to_proc:
            res = self.__build_op(i, self.__data)
            per = counter // self.data_size
            if per != toggle and progress and per % prog_rate == 0:
                print(f"{per}% have been processed.")
                toggle = per
            counter += 1
            self.graph.update(res)
        return self.graph

    def search(self, id: str):
        """Search graph."""
        if self.graph is not None and self.__data is not None:
            matches = self.graph[id]
            fetched_data = list(map(lambda x: self.__data[x], matches))
            return self.__data[id], fetched_data
        else:
            return None, None

    def add(self, elements: dict):
        """Add element."""
        if list(elements.keys()) in self.__data_to_proc:
            return None
        self.__data.update(elements)
        self.__create_data(self.__data)
        for k in list(elements.keys()):
            matches = self.__build_op(k, self.__data)
            self.graph.update(matches)

    def load(self, graph_path: str):
        """Load graph dict from json file."""
        with open(graph_path, 'r+') as graph_file:
            self.graph = json.load(graph_file)

    def save(self, graph_path: str, indent: int):
        """Save graph as json."""
        with open(graph_path, 'w+') as graph_file:
            json.dump(self.graph, graph_file, indent=indent)
        return self.graph

    def get(self, id: str):
        """Get element from data."""
        if self.__data is not None:
            return self.__data.get(id)
        return None

    @property
    def data(self):
        """Getter for data."""
        return self.__data
