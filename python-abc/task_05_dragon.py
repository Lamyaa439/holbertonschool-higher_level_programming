#!/usr/bin/env python3
"""
This module demonstrates the Mixin pattern in Python.
It defines modular behaviors (Swim and Fly) that can be 
composed into a single Dragon class.
"""


class SwimMixin:
    """Provides swimming behavior."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Provides flying behavior."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that composes behaviors from multiple Mixins.
    It also includes its own unique behavior.
    """
    def roar(self):
        print("The dragon roars!")
