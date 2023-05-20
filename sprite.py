class Sprite:
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char
    def update(self):
        self.move(0, 0)
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def collide(self, obj):
        pass