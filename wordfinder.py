"""Word Finder: finds random words from a dictionary."""

#python -m doctest -v file.py

from random import seed, choice

class WordFinder:
    """
    A class used to return a random word from a file containing a list of words

    Attributes
    ----------
    path: str
        path to a file on disk
    words: list
        list containing list of words from file
    words_read: int
        number of elements read from file successfully placed in words list

    >>> wf = WordFinder('words.txt')
    235886 words read

    >>> wf.random(1)
    choler

    >>> wf.random(10)
    polis

    >>> wf.random(100)
    coaration
    """

    def __init__(self, path):
        self.path = path
        self.words = []
        self.words_read = self.read_file()
        print(f"{self.words_read} words read")

    def read_file(self):
        """Reads file on disk and makes an a list of words contained in file"""
        try:
            with open(self.path, 'r') as file:
                for line in file:
                    self.words.append(line.rstrip('\n'))
            file.close()
            return len(self.words)
        except OSError as ex:
            self.words = []
            print(f"Unable to open {self.path}: {ex}")
            return 0
        
    def random(self, seed_val=None):
        """Returns a random word from list of words"""
        try:
            seed(seed_val)
            print(choice(self.words))
        except IndexError as ex:
            print(f"Unable to read from words list: {ex}")

        # except Exception as ex:
        #     template = "An exception of type {0} occurred."
        #     message = template.format(type(ex).__name__)
        #     print(message)
            