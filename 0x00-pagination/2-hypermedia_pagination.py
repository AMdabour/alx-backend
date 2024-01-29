#!/usr/bin/env python3
""" a function that takes two integer arguments page and page_size
to return the range of indexes in a list for those particular
pagination parameters.
"""
from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index"""
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
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
        """returns the data of a specifiec page"""
        try:
            assert isinstance(page, int) and page > 0
            assert isinstance(page_size, int) and page_size > 0
            dataset = self.dataset()
            start_index, end_index = index_range(page, page_size)
            if end_index <= len(dataset):
                return dataset[start_index:end_index]
            else:
                return []
        except Exception:
            raise AssertionError

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """hypermedia pagination"""
        page_data = self.get_page(page, page_size)
        start_indx, end_indx = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_info: Dict = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if end_indx < total_pages else None,
            'prev_page': page - 1 if start_indx > 1 else None,
            'total_pages': total_pages
        }

        return page_info
