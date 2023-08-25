#!/usr/bin/env python3
'''1-simple_pagination'''

import csv
from typing import List, Tuple


class Server:
    '''Server class to paginate a database of popular baby names.'''
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Paginates the dataset building the list of rows'''
        assert (
                (type(page) == int and page > 0)
                and (type(page_size) == int and page_size > 0)
        )
        start, end = index_range(page, page_size)
        if self.__dataset is None\
            or type(self.__dataset) is List[List]\
                and len(self.__dataset) == 0:
            self.__dataset = self.dataset()
        return self.__dataset[start:end]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Considering a page number and maximum number of items per page,
    computes a tuple that holds the start and end index of a page
    Args:
        page: number of a page. Page number @page
        page_size: number of items per page
    Return:
        a tuple of indexes'''
    start = page * page_size - page_size
    end = page * page_size
    return (start if start >= 1 else 0, page * page_size)
