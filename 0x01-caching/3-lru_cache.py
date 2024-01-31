#!/usr/bin/env python3
"""LRUCache class as a caching system"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """the caching system"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.lru_list = []

    def put(self, key, item):
        """put a value to a key in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if key in self.lru_list:
            self.lru_list.remove(key)
        self.lru_list.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lruItem = self.lru_list[0]
            del self.cache_data[lruItem]
            self.lru_list.remove(lruItem)
            print("DISCARD:", lruItem)

    def get(self, key):
        """get a value for a key from the cache"""
        if key in self.lru_list:
            self.lru_list.remove(key)
            self.lru_list.append(key)
        return self.cache_data.get(key, None)
