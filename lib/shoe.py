#!/usr/bin/env python3
class Shoe:
    def __init__(self, brand, size=0):
        self.brand = brand
        self.size = size
        self.condition = None

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    def get_size(self):
        return self.size

    def set_size(self, value):
        if type(value) == int:
            self.size = value
        print("size must be an integer")

    size = property(get_size, set_size)




