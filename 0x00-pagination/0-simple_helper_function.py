#!/usr/bin/env python3
'''0-simple_helper_function'''

from typing import Tuple


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
