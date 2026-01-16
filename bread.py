import op_arcade as oa
import op_arcade.constants_classes as cc
import os
import random
import arcade
from arcade import Sound

from level_base import LevelBase
from sprites import   sub, Player, bread

# =====================================
# get the file locaion to ware to find it

def get_asset_path(filename, subfolder="images"):
    base = os.path.dirname(__file__)  # folder where your script lives
    return os.path.join(base, subfolder, filename)
    
def get_music_path(filename, subfolder="sounds"):
        base = os.path.dirname(__file__)  # folder where your script lives
        return os.path.join(base, subfolder, filename)

class bread(oa.View):
    


    def on_create(self):

        # self.add_default_layers()

        self.items_collected = 0 # set the collectde items vabl to 0


        self.background_color = cc.Colors.BROWN_NOSE # the background coloor
        # ===================================
        # Sprites 
        self.player = Player(100, 200)
        bread
        #================================== 
        # WALLS
        # floor{ 
        BRIDGE_TILE_WIDTH = 128 # For readability, we use a constant to specify the width of the bridge tile

        for x in range(0, BRIDGE_TILE_WIDTH*345, BRIDGE_TILE_WIDTH):
            oa.Sprite(x, 20, ":resources:/images/tiles/bridgeB.png", cc.Layers.WALLS)
        # }

        # =============================================
    def on_step(self):

        self.clear()
        self.scene.draw()
        self.draw_grid()



        

oa.run(bread, title="moon gravity platformer game")