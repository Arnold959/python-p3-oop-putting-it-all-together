#!/usr/bin/env python3

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publication_year(self):
        return self.publication_year
    pass
    
        