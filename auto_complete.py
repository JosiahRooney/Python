class Trie(object):
    def __init__(self):

    def add_word(self):

    def has_word(self):

    def print_word_starting_with(self):


class Node(object):
    def __init__(self, value, isWord):
        self.value = value
        self.isWord = isWord
        self.children = []


