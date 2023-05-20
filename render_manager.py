import os

class RenderManager:
    def __init__(self, width, height, box="", collision_callback=None):
        self.objects = []
        self.map = []
        self.width = width
        self.height = height
        self.box = box
        self.collision_callback = collision_callback
    def update(self):
        for obj in self.objects:
            obj.update()
        self.map = [[None for i in range(self.width)] for i in range(self.height)]
        for obj in self.objects:
            if obj.y < 0 or obj.y >= self.width or obj.x < 0 or obj.x >= self.height:
                self.objects.remove(obj)
                continue
            elif self.map[obj.x][obj.y] != None:
                if self.collision_callback:
                    self.collision_callback(self.map[obj.x][obj.y], obj)
                continue
            self.map[obj.x][obj.y] = obj
    def render(self):
        os.system("cls")
        for l in reversed(self.map):
            print(self.box, end="")
            for i in l:
                if i != None:
                    print(i.char, end="")
                else:
                    print(" ", end="")
            print(self.box)
    def add(self, obj):
        self.objects.append(obj)
    def remove(self, obj):
        self.objects.remove(obj)