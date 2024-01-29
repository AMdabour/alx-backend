#!/usr/bin/env python3
""" a function that takes two integer arguments page and page_size
to return the range of indexes in a list for those particular
pagination parameters.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index"""
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size
    return (start_index, end_index)
