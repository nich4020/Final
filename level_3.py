import op_arcade as oa
import op_arcade.constants_classes as cc
import os
import random
import arcade
from arcade import Sound

from level_base import LevelBase
from sprites import  dog, BlueBird, Coin, vista_orb, sub

# =====================================
# get the file locaion to ware to find it

def get_asset_path(filename, subfolder="images"):
    base = os.path.dirname(__file__)  # folder where your script lives
    return os.path.join(base, subfolder, filename)
    
def get_music_path(filename, subfolder="sounds"):
        base = os.path.dirname(__file__)  # folder where your script lives
        return os.path.join(base, subfolder, filename)
class Level_3(oa.View):
    


    def on_create(self):
        self.background = oa.Sprite(4000, 1900, get_asset_path("XP.png"), layer=cc.Layers.BACKGROUND, scale=2) # the Background
        self.add_sf_map_layers("Maps/Untitled", scale=2)
        # self.add_default_layers()

        self.items_collected = 0 # set the collectde items vabl to 0
        # ===============================
        # Randomly choise the BGM and play the music
        bgm = random.choice([get_music_path("title.wma"), get_music_path("Wii sports resort music_ Main theme.mp3"), get_music_path("Nintendo Switch 2 Setup Music.m4a"), get_music_path("Training Menu_ Activity Selection - Wii Fit Soundtrack.mp3"), get_music_path("TV Channel Menu - TV Friend Channel.mp3"), get_music_path("Nintendo DSi Shop.m4a"), get_music_path("Friend List - Wii U Menu Music.mp3")])
        self.music = Sound(bgm, streaming=True)
        self.music.play()
        # ==================================
        self.world_camera = oa.Camera() # Create a camera to allow for scrolling
        # ===================================
        self.background_color = cc.Colors.GO_GREEN # the background coloor
        # ===================================
        # Sprites 
        self.player = Player(100, 200)
        sub(600, 300, group="collectable")
        oa.Sprite(1050, 700, get_asset_path("日本.png"), group="collectable")
        oa.Sprite(900, 250, get_asset_path("duck.png",  subfolder="images"))
        for y in range(900, 600, -90):
            Coin(600, y, group="collectable")
        for i in range(60):
            dog(random.randint(50, 1400), random.randint(50, 1250))
        #================================== 
        # WALLS
        # floor{ 
        BRIDGE_TILE_WIDTH = 128 # For readability, we use a constant to specify the width of the bridge tile
        # self.create_vwall(790, 600, 5, get_asset_path("Vista.png",  subfolder="images"), scale=0.3)
        # self.create_vwall(0, 50, 100, get_asset_path("Vista.png",  subfolder="images"), scale=0.3)
        # self.create_vwall(900, 800, 8, get_asset_path("Vista.png",  subfolder="images"), scale=0.3)
        
        # Add the bottom bridge platform (20 tiles in a row)
        # for x in range(0, BRIDGE_TILE_WIDTH*345, BRIDGE_TILE_WIDTH):
        #     oa.Sprite(x, 20, ":resources:/images/tiles/bridgeB.png", cc.Layers.WALLS)
        for x in range(0, BRIDGE_TILE_WIDTH*345, BRIDGE_TILE_WIDTH):
            oa.Sprite(x, 3900, ":resources:/images/tiles/bridgeB.png", cc.Layers.WALLS)
        # }
        # platform 
        
        # Add the upper bridge platform (1 tile only)
        # oa.Sprite(800, 150, ":resources:/images/tiles/bridgeA.png", cc.Layers.WALLS)
        # oa.Sprite(1000, 250, ":resources:/images/tiles/bridgeA.png", cc.Layers.WALLS)
        # oa.Sprite(700, 530, ":resources:/images/tiles/bridgeA.png", cc.Layers.WALLS)
        # oa.Sprite(900, 590, ":resources:/images/tiles/bridgeA.png", cc.Layers.WALLS)
        # =============================================
    def on_step(self):
        # Make the camera follow the player
        self.world_camera.center_on_sprite(self.player, left_bound=0, lower_bound=-0, right_bound=8000, upper_bound=3950)
        self.world_camera.use()

        self.clear()
        self.scene.draw()
        self.draw_grid()


class Player(oa.Sprite):

    def on_create(self):
        # ================================================
        self.visual = (get_asset_path("Windows_xp.jpg"))
        self.scale = 0.3
        # ================================
        # self.layer = cc.Layers.MOVING_GAME_OBJECT
        self.bind_platformer_directional_keys() # Notice this time, we use the **platformer** directional keys
        self.enable_physics(gravity=0.01) #This is where we enable gravity for a platformer game
    def on_step(self):
        #Handle a collision with a collectable item
        colliding_item = self.find_colliding("collectable")
        if colliding_item:
            self.view.items_collected += 1
            colliding_item.kill()
            COIN_SOUND = arcade.load_sound(get_music_path("ding.wav"))
            self.coin_playback = arcade.play_sound(COIN_SOUND)
        
        colliding_enemy = self.find_colliding("enemy")  
        if colliding_enemy:
            # reduce health by damage given
            hurt_SOUND = arcade.load_sound(get_asset_path("chord.wav",  subfolder="sounds"))
            self.coin_playback = arcade.play_sound(hurt_SOUND)
            self.health -= colliding_enemy.damage_given
            self.x = 50
            self.y = 50
        

oa.run(Level_3, title="moon gravity platformer game")