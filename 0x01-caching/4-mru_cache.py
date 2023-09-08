#!/usr/bin/env python3

"""4-mru_cache module"""
from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """MRU cache system implementation"""

    def __init__(self):
        """Initializes a new FIFOCache instance"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.__access = []

    def put(self, key, item):
        """Adds a new item in the cache"""
        if key and item:
            self.cache_data[key] = item
            if key in self.__access:
                self.__access.remove(key)
            self.push(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                d = self.pop()
                print(f'DISCARD: {d}')
                del self.cache_data[d]

    def get(self, key):
        """Gets an existing item from the cache"""
        if key in self.cache_data and key in self.__access:
            self.__access.remove(key)
            self.push(key)
        return self.cache_data.get(key, None)

    def push(self, key):
        ''' Adds an element to the top of the list'''
        self.__access.append(key)
        self.__access[-1], self.__access[0] = (self.__access[0],
                                               self.__access[-1])

    def pop(self):
        '''Removes and returns the element at the end of the list'''
        return self.__access.pop() if len(self.__access) > 0 else None
