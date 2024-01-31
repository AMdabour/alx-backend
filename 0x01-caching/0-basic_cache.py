# !/usr/bin/env python3
"""BasicCache class as a caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """the caching system"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """put an item to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get a calue for a key from the cache"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
