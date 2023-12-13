from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """
    A subclass of WordFinder used to return a random word from a file containing a list of words (words must not begin with '#' or be blank spaces)

    >>> swf = SpecialWordFinder('special_words.txt')
    4 words read

    >>> swf.random(1)
    parsnips

    >>> swf.random(2)
    kale
    """

    def __init__(self, path):
        super().__init__(path)

    def read_file(self):
        """Reads file on disk and makes an a list of specific words contained in file"""
        try:
            with open(self.path, 'r') as file:
                for line in file:
                    if not line.strip().startswith('#') and line.strip() != '':
                        self.words.append(line.rstrip('\n'))
            file.close()
            return len(self.words)
        except OSError as ex:
            self.words = []
            print(f"Unable to open {self.path}: {ex}")
            return 0