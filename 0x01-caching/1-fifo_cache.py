# !/usr/bin/env python3
"""FIFOCache as a caching system"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """the caching system"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """"put an item for a key in the cache using FIFO algorithm"""
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                return
            elif len(self.cache_data) == self.MAX_ITEMS:
                # mykeys = list(self.cache_data.key())
                # del self.cache_data[mykeys[0]]
                firstItem = next(iter(self.cache_data))
                del self.cache_data[firstItem]
                print(f"DISCARD: {firstItem}")
            self.cache_data[key] = item

    def get(self, key):
        """get the value of the key in the cache"""
        if key is None or key not in self.cache_data.key():
            return None
        return self.cache_data[key]
