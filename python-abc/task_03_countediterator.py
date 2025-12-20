#!/usr/bin/env python3
"""
This module defines the CountedIterator class.
It wraps an iterator and keeps track of how many items have been processed.
"""


class CountedIterator:
    """
    An iterator wrapper that counts the number of items iterated over.
    """

    def __init__(self, iterable):
        """
        Initializes the CountedIterator with an iterable.
        
        Args:
            iterable: Any Python object that can be iterated over.
        """
        self.iterator = iter(iterable)
        self.__count = 0

    def get_count(self):
        """Returns the current number of items iterated."""
        return self.__count

    def __next__(self):
        """
        Increments the counter and returns the next item from the iterator.
        
        Raises:
            StopIteration: If there are no more items to iterate.
        """
        try:
            item = next(self.iterator)
            self.__count += 1
            return item
        except StopIteration:
            # We don't increment the count if StopIteration is raised
            raise StopIteration

    def __iter__(self):
        """Returns the iterator object itself."""
        return self
