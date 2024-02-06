#!/usr/bin/env python3
"""LIFOCache as a caching system"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """the caching system"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """put a value to a key in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            self.cache_data[key] = item
            return
        elif len(self.cache_data) == BaseCaching.MAX_ITEMS:
            lastItem, _ = self.cache_data.popitem()
            print("DISCARD:", lastItem)
        self.cache_data[key] = item

    def get(self, key):
        """get an item from the cache by its key"""
        return self.cache_data.get(key, None)
