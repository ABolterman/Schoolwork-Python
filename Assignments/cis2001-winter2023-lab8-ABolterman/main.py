# Adapted from https://github.com/EricCharnesky/CIS2001-Winter2023/blob/main/Week11-Maps/main.py

class Book:
    def __init__(self, title, isbn, authors):
        self._title = title
        self._isbn = isbn
        self._authors = authors

    def __hash__(self):
        return hash(self._isbn)


class Library:
    class Pair:

        def __init__(self, key, value=None):
            self.key = key
            self.value = value

        def __eq__(self, other):
            return self.key == other.key

        def __ne__(self, other):
            return not self == other

        def __str__(self):
            return str(self.key) + ": " + str(self.value)

    def __init__(self):
        self._data = [None]*11
        self._number_of_items = 0

    def add_book(self, key, value=None):
        index = self._get_index_in_hash_table(key)
        if self._data[index] is None:
            self._data[index] = [self.Pair(key, value)]  # start a list with 1 pair
            self._number_of_items += 1
        else:
            for pair in self._data[index]:
                if pair.key == key:
                    pair.value = value
                    return
            self._data[index].append(self.Pair(key, value))
            self._number_of_items += 1

    def check_out(self, key):
        index = self._get_index_in_hash_table(key)
        if self._data[index] is None:
            raise KeyError
        item = self.Pair(key)
        for pair in self._data[index]:
            if pair == item:
                self._data[index].remove(item)
                self._number_of_items -= 1
                return item
        raise KeyError

    def lookup(self, lookup_info):
        for index in range(len(self._data)):
            for jndex in range(len(self._data[index])):
                book = self._data[index][jndex]
                if type(lookup_info) is str: #titles are strings
                    if book._title == lookup_info:
                        return book
                if type(lookup_info) is int: #ISBN are integers
                    if book._isbn == lookup_info:
                        return book
                if type(lookup_info) is list:
                    if lookup_info in book._authors:
                        return book
        raise LookupError("Book not found")

    def _get_index_in_hash_table(self, key):
        return hash(key) % len(self._data)