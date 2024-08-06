"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Finds words from a given txt document."""

    def __init__(self, path):
        "Creates a WordFinder object with the given path to a txt document."
        self.path = path
        self.words = self.make_list()
        self.num_words()

    def make_list(self):
        "Makes an attribute list of the words found in the txt document." 
        words = []
        file = open(self.path, 'r')
        for line in file:
            line = line.strip()
            words.append(line)
        file.close()
        return words
    
    def num_words(self):
        "Returns the number of words found in the given txt document."
        num_words = len(self.words)
        print(f"{num_words} words read")

    def random(self):
        "Returns a random word from the list of words created from the txt document."
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Finds words from a given txt document that has comments and spaces"""
    def __init__(self, path):
        super().__init__(path)
    
    def make_list(self):
        words = []
        file = open(self.path, 'r')
        for line in file:
            line = line.strip()
            if line and line[0].isalpha():
                words.append(line)
        file.close()
        return words
