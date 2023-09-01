#!/usr/bin/env python3

"""1-fifo_cache module"""
from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache system implementation"""
    def __init__(self):
        """Initializes a new FIFOCache instance"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds a new item in the cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = list(self.cache_data.keys())[0]
                print(f"DISCARD: {discarded}")
                del self.cache_data[discarded]

    def get(self, key):
        """Gets an existing item from the cache"""
        return self.cache_data.get(key, None)
