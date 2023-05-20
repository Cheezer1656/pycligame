import os

class TextObject:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

class MenuRenderManager:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objects = []
        self.map = []
    def add(self, obj):
        self.objects.append(obj)
    def remove(self, obj):
        self.objects.remove(obj)
    def update(self):
        # Make TextObjects into a map
        self.map = [[None for i in range(self.width)] for i in range(self.height)]
        for obj in self.objects:
            for char in obj.text:
                pass # DO STUFF
    def render(self):
        os.system("cls")
        for i in range(self.height):
            for obj in self.objects:
                if obj.y == i:
                    print(" "*obj.x+obj.text, end="")
            print()

class MenuScene:
    def __init__(self, width, height):
        self.rm = MenuRenderManager(width, height)
        self.width = width
        self.height = height
        self.objects = []
    def get_height(self):
        return self.height
    def get_width(self):
        return self.width
    def add_text(self, obj):
        self.objects.append(obj)
        self.rm.add(obj)
    def remove_text(self, obj):
        self.objects.remove(obj)
        self.rm.remove(obj)
    def mainloop(self):
        self.rm.render()
        input()