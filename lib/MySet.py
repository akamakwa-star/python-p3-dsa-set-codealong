
class MySet:
    def __init__(self, iterable=None):
        self.dictionary = {}
        if iterable:
            for item in iterable:
                self.dictionary[item] = True

    def add(self, item):
        self.dictionary[item] = True

    def delete(self, item):
        if item in self.dictionary:
            del self.dictionary[item]

    def has(self, item):
        return item in self.dictionary
