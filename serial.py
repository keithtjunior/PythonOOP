"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        self.start = start
        self.current = start

    def generate(self):
        """Returns next sequential number of provided start number (beginning with start number)"""
        try:
            return self.current
        finally:
            self.current = self.current+1
    
    def reset(self):
        "Resets current number to start number"
        self.current = self.start