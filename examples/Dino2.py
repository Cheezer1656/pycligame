from pycligame import Sprite, Scene, MenuScene, Script, TextObject, ExitGame
from random import randint

class Dino(Sprite):
    def __init__(self, x, y, height):
        self.up = 0
        self.height = height
        super().__init__(x, y, "/")
    def update(self):
        if self.up > 0 and self.x < self.height-1:
            self.move(1, 0)
            self.up -= 1
        elif self.up == 0 and self.x > 0:
            self.move(-1, 0)
    def jump(self):
        if self.up == 0 and self.x == 0:
            self.up = self.height-1

class Cactus(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, ".")
    def update(self):
        self.move(0, -1)

class GameManager(Script):
    def __init__(self, scene):
        self.frames_since_last_obstacle = 0
        self.score = 0
        super().__init__(scene)
    def pre_update(self):
        if randint(0, 10) == 0:
            if self.frames_since_last_obstacle > 5:
                self.scene.add_sprite(Cactus(0, scene.get_width()))
                self.frames_since_last_obstacle = 0
    def post_render(self):
        print(self.scene.rm.box+"-"*self.scene.get_width()+self.scene.rm.box)
        print("Score:", self.score)
        # --- DEBUG ---
        #global player
        #print("player.up =", player.up)
        #print("player.x =", player.x)
        # --- DEBUG ---
        self.score += 1
        self.frames_since_last_obstacle += 1
    def collision(self, obj1, obj2):
        if obj1 == player or obj2 == player:
            raise ExitGame()

width = 50
height = 3

scene = MenuScene(width, height)
scene.add_text(TextObject(0, 0, "Dino - CLI Version"))
scene.add_text(TextObject(0, 1, "Press space to jump"))
scene.mainloop()

while True:
    scene = Scene(width, height, "#")
    player = Dino(0, 2, scene.get_height())
    scene.add_sprite(player)
    scene.bind("space", player.jump)
    scene.add_script(GameManager(scene))

    scene.mainloop(0.25)

    print("\nGAME OVER")
    input("Press enter to try again")