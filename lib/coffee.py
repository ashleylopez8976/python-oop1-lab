#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        # Store the size and price for this coffee.
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Only store one of the three allowed sizes.
        if value in ("Small", "Medium", "Large"):
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        # Add a one-dollar tip and display a message.
        self.price += 1
        print("This coffee is great, here’s a tip!")