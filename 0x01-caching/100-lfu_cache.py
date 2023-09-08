#!/usr/bin/env python3

"""100-lfu_cache.py module"""
from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """LFU cache system implementation"""

    def __init__(self):
        """Initializes a new FIFOCache instance"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.__access = OrderedDict()

    def put(self, key, item):
        """Adds a new item in the cache"""
        if key and item:
            self.cache_data[key] = item

            if len(self.__access) > 0 and len(self.cache_data) > 0:
                self.__access = OrderedDict(sorted(self.__access.items(),
                                            key=lambda item: item[1]))
                discarded = list(self.__access.keys())[0]
            else:
                discarded = None

            if key in self.__access and key in self.cache_data:
                self.__access[key] += 1
                self.__access.move_to_end(key, True)
            else:
                self.__access[key] = 1
                self.__access.move_to_end(key, True)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print(f'DISCARD: {discarded}')
                del self.cache_data[discarded]
                del self.__access[discarded]

    def get(self, key):
        """Gets an existing item from the cache"""
        if key in self.cache_data and key in self.__access:
            self.__access[key] += 1
            self.__access.move_to_end(key, True)
        return self.cache_data.get(key, None)
