#!/usr/bin/env python3
"""LFUCache class as a caching system"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """the caching system"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.dict = OrderedDict()

    def put(self, key, item):
        """put a value to a key in the cache"""
        if key is None or item is None:
            return
        if key in self.dict.keys():
            self.dict[key] = self.dict.get(key, 0) + 1
            self.cache_data[key] = item
            return
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            target = min(self.dict.values())
            lfuItem = [key for key,
                       value in self.dict.items() if value == target]
            if len(lfuItem) > 1:
                for keyc in self.cache_data.keys():
                    for value in lfuItem:
                        if keyc == value:
                            del self.cache_data[value]
                            del self.dict[value]
                            print("DISCARD:", value)
                            self.cache_data[key] = item
                            self.dict[key] = self.dict.get(key, 0) + 1
                            return
            del self.cache_data[lfuItem[0]]
            del self.dict[lfuItem[0]]
            print("DISCARD:", lfuItem[0])
        self.cache_data[key] = item
        self.dict[key] = self.dict.get(key, 0) + 1

    def get(self, key):
        """get a value og a key from the cache"""
        if key in self.dict.keys():
            self.dict[key] = self.dict.get(key, 0) + 1
        return self.cache_data.get(key, None)
