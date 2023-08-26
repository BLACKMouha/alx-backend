#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''Check changes of __indexed_dataset and retrieves data accordingly'''
        assert ((type(index) is int and index > -1
                 and index < len(self.dataset()))
                and (type(page_size) is int and page_size > 0))
        indexed_dataset = self.__indexed_dataset
        self.__dataset = []
        for k in indexed_dataset.values():
            self.__dataset.append(k)
        end = index + page_size
        if end > len(indexed_dataset):
            end = None
        data = list(indexed_dataset.values())[index:end]
        tmp_index = index + page_size
        if tmp_index < len(indexed_dataset):
            next_index = list(indexed_dataset.keys())[index + page_size]
        else:
            next_index = list(indexed_dataset.keys())[-1]
        if next_index == index:
            next_index = None
        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
