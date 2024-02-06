#!/usr/bin/env python3
"""MRUCache class as a caching system"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """the caching system"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.mru_list = []

    def put(self, key, item):
        """put a value to a key in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if key in self.mru_list:
            self.mru_list.remove(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mruItem = self.mru_list[-1]
            del self.cache_data[mruItem]
            self.mru_list.remove(mruItem)
            print("DISCARD:", mruItem)
        self.mru_list.append(key)

    def get(self, key):
        """get an item from the cache by its key"""
        if key in self.mru_list:
            self.mru_list.remove(key)
            self.mru_list.append(key)
        return self.cache_data.get(key, None)
