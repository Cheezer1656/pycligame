from .render_manager import RenderManager
from .errors import ExitGame
from time import sleep
import keyboard as k

class Scene:
    def __init__(self, width, height, box=""):
        self.rm = RenderManager(width, height, box, self.collision)
        self.objects = []
        self.scripts = []
        self.keybinds = []
    def get_height(self):
        return self.rm.height
    def get_width(self):
        return self.rm.width
    def add_sprite(self, obj):
        self.objects.append(obj)
        self.rm.add(obj)
    def remove_sprite(self, obj):
        self.objects.remove(obj)
        self.rm.remove(obj)
    def add_script(self, script):
        self.objects.append(script)
        self.scripts.append(script)
    def remove_script(self, script):
        self.objects.remove(script)
        self.scripts.remove(script)
    def collision(self, obj1, obj2):
        for script in self.scripts:
            script.collision(obj1, obj2)
    def bind(self, key, callback):
        self.keybinds.append((key, callback))
    def unbind(self, key):
        for i in self.keybinds:
            if i[0] == key:
                self.keybinds.remove(i)
    def mainloop(self, refresh_rate):
        for i in self.keybinds:
            k.add_hotkey(i[0], i[1])
        try:
            while True:
                for script in self.scripts:
                    script.pre_update()
                self.rm.update()
                for script in self.scripts:
                    script.post_update()
                for script in self.scripts:
                    script.pre_render()
                self.rm.render()
                for script in self.scripts:
                    script.post_render()
                sleep(refresh_rate)
        except ExitGame:
            pass
        for i in self.keybinds:
            k.remove_hotkey(i[0])