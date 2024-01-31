#!/usr/bin/env python3
"""FIFOCache as a caching system"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """the caching system"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """"put an item for a key in the cache using FIFO algorithm"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # mykeys = list(self.cache_data.keys())
                # del self.cache_data[mykeys[0]]
                firstItem = next(iter(self.cache_data))
                del self.cache_data[firstItem]
                print("DISCARD:", firstItem)

    def get(self, key):
        """get the value of the key in the cache"""
        return self.cache_data.get(key, None)
