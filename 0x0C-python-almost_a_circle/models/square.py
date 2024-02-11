# models/square.py

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance with size, x, y, and id"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign attributes using *args and **kwargs"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, val in zip(attrs, args):
                setattr(self, attr, val)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def __str__(self):
        """Return string representation of the Square instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
