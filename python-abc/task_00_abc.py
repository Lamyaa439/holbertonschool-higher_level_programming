#!/usr/bin/env python3
"""
This module defines Abstract Animal Class and its Subclasses
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    This is the Animal class
    """
    @abstractmethod
    def sound(self):
        """
        the sound method
        """
        pass


class Dog(Animal):
    """
    This is a subclass named Dog that inherits from the Animal class.
    """
    def sound(self):
        """
        method to return the string (Bark).
        """
        return "Bark"


class Cat(Animal):
    """
    This is a subclass named Cat that also inherits from the Animal class.
    """
    def sound(self):
        """
        method to return the string (Meow).
        """
        return "Meow"
