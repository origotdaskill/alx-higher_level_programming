# models/square.py

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance with size, x, y, and id"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size attribute"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of the Square instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
