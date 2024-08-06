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
    def __init__(self, start):
        "Create serial number."
        self.start = start
        self.first = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.start + 1}>"

    def generate(self):
        "Generate serial number (from start)."
        num = self.start
        self.start += 1
        return num
    
    def reset(self):
        "Resets serial number to starting number."
        self.start = self.first
    