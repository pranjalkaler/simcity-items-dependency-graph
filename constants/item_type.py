from enum import Enum

class Type(Enum):
    INDUSTRIAL = 1
    COMMERCIAL = 2

    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)