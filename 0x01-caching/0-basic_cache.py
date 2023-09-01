#!/usr/bin/env python3
"""0-basic_cachinh module"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
	"""BasicCache class inherits from BaseCachong and pverwrite its methods"""
	def put(self, key, item):
		"""Adds a new item in te cache"""
		if key:
			self.cache_data[key] = item

	def get(self, key):
		"""Retrieves an item from the cache"""
		return self.cache_data.get(key, None)

