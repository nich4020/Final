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

        #================================== 
        # WALLS
        # floor{ 
        BRIDGE_TILE_WIDTH = 128 # For readability, we use a constant to specify the width of the bridge tile

        for x in range(0, BRIDGE_TILE_WIDTH*345, BRIDGE_TILE_WIDTH):
            oa.Sprite(x, 20, ":resources:/images/tiles/bridgeB.png", cc.Layers.WALLS)
        # }

        # =============================================
    def on_step(self):
        if random.randint(0, 60) == 0:
            breads(100, 300, group="enemy_projectiles")
        self.clear()
        self.scene.draw()
        self.draw_grid()
        if random.randint(0, 1100) == 0:
            oa.Sprite(10, int(self.player.x + random.randint(200, 2000)), get_asset_path("falling-Bread.png"), group="call")


class breads(oa.Sprite):

    def on_create(self):
        slice = random.choice([get_asset_path("Bread.jpg"), get_asset_path("bread-pictures.jpg"), get_asset_path("milk-bread.jpg"), get_asset_path("sliced-bread.jpg"), get_asset_path("sliced-french-bread.jpg"), get_asset_path("Homemade-Bread.jpg"), get_asset_path("maxresdefault-3596983426.jpg"), get_asset_path("SUB.png"), get_asset_path("wheat-bread.jpg"), get_asset_path("whole-wheat-bread.jpg")])
        jhgfd = slice
        self.visual = jhgfd
        self.scale = 0.5
        self.layer = cc.Layers.MOVING_GAME_OBJECTS
        self.change_x = 8
        # vista_orb_sOUND = arcade.load_sound("Local/Unit 4/part1/sounds/Windows Shutdown.wav")
        # vista_orb_play = arcade.play_sound(vista_orb_sOUND)


    def on_step(self):
        # If we've gone off screen, remove ourself from the game.
        # It's important to remember this step, or otherwise the game will eventually
        # slow down and it's trying to render a bunch of arrows off screen
        if self.x == 1600:
            self.kill() 
        # # refs.cur_view.world_camera.point_in_view(int(self.x), int(self.y)) == False:
        #     self.kill()
        

oa.run(bread, title="moon gravity platformer game")