#!/usr/bin/env python3

"""2-lifo_cache module"""
from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cache system implementation"""
    __num_items = 0

    def __init__(self):
        """Initializes a new FIFOCache instance"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds a new item in the cache"""
        if key and item:
            if key in self.cache_data:
                self.cache_data.update({key: item})
                return
            self.cache_data[key] = item
            if BaseCaching.MAX_ITEMS % 2 == 0:
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    self.__num_items += 1
                    if self.__num_items * 2 > BaseCaching.MAX_ITEMS:
                        self.__num_items = 1
                    discarded = list(
                        self.cache_data.keys())[-self.__num_items - 1]
                    print(f"DISCARD: {discarded}")
                    del self.cache_data[discarded]
            else:
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    discarded = list(self.cache_data.keys())[-2]
                    print(f"DISCARD: {discarded}")
                    del self.cache_data[discarded]

    def get(self, key):
        """Gets an existing item from the cache"""
        return self.cache_data.get(key, None)
