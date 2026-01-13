# Import external libraries
import arcade
import op_arcade as oa
import op_arcade.constants_classes as cc
import os
import random
# Import items from our own files
from level_base import LevelBase
from sprites import Player, Fly, BlueBird, Coin, FireBall

# This class extends LevelBase, which provides common functionality for all levels
class Level_2(LevelBase):

    # Include this method in every level, and make sure it references the correct map
    def layer_setup(self):
        self.add_sf_map_layers("maps/level_2", scale=3)
        self.add_default_layers()

    def on_create(self):
        # This will run the level_setup method in level_base.py
        self.level_setup()
        # self.fireball_timer = oa.Timer(2.0, True)
        # self.fireball_timer.start()
        self.draw_grid()
        self.player = Player(400, 300)
        for i in range(60):
            Fly(random.randint(50, 1400), random.randint(50, 1250))
        BlueBird(200, 400)

        # This will add a row of coins
        for x in range(600, 16, 80):
            Coin(x, 700, group="collectable")

        for y in range(900, 600, -90):
            Coin(600, y, group="collectable")
        
    
    def on_step(self):
        super().on_step()
        self.world_camera.center_on_sprite(self.player)
        self.world_camera.use()
        self.clear()

        # ✅ This updates ALL sprites (Player, Fly, FireBall, etc.)

        self.scene.draw()
        # ✅ Spawn fireballs during gameplay
        if random.randint(0, 60) == 0:
            FireBall(-10, int(self.player.y + random.randint(-200, 200)), group="enemy_projectiles")


# Include this for every level, ensure the correct level is being run
if __name__ == "__main__":
    oa.run(Level_2, title="Level 2 kill the flying Buddy with the error or the secret weapon (B) Key on your keyboard!")