#!/usr/bin/env python3
"""
This module defines the VerboseList class which extends the built-in list.
It provides notifications when the list is modified.
"""


class VerboseList(list):
    """
    A custom list class that prints messages when items are added or removed.
    """

    def append(self, item):
        """Adds an item and prints a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Extends the list and prints the count of items added."""
        item_count = len(items)
        super().extend(items)
        print(f"Extended the list with [{item_count}] items.")

    def remove(self, item):
        """Prints a notification before removing a specific item."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Prints a notification before popping an item.
        Defaults to the last item if no index is provided.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
