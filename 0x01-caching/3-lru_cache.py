#!/usr/bin/env python3

"""3-lru_cache module"""
from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """LRU cache system implementation"""

    def __init__(self):
        """Initializes a new FIFOCache instance"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.__access = []  # a queue

    def put(self, key, item):
        """Adds a new item in the cache"""
        if key and item:
            self.cache_data[key] = item
            if key in self.__access:
                i = self.__access.index(key)
                k = self.__access.pop(i)
                self.enqueue(k)
            else:
                self.enqueue(key)
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    d = self.dequeue()
                    print(f'DISCARD: {d}')
                    del self.cache_data[d]

    def get(self, key):
        """Gets an existing item from the cache"""
        if key in self.cache_data and key in self.__access:
            i = self.__access.index(key)
            k = self.__access.pop(i)
            self.__access.append(k)
        return self.cache_data.get(key, None)

    def enqueue(self, key):
        ''' Adds an element to the end of the list'''
        if key:
            self.__access.append(key)

    def dequeue(self):
        '''Removes and returns the element at the front of the list'''
        return self.__access.pop(0) if len(self.__access) > 0 else None
