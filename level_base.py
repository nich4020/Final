# Import external libraries
import arcade
import op_arcade as oa
import op_arcade.constants_classes as cc
import os 
def get_asset_path(filename, subfolder="assets"):
        base = os.path.dirname(__file__)  # folder where your script lives
        return os.path.join(base, subfolder, filename)
    
# Import items from our own files
from sprites import bliss, err

# This class contains code that is common to ALL levels
class LevelBase(oa.View):

    def level_setup(self):
        # Set up cameras
        self.world_camera = oa.Camera()
        self.dashboard_camera = oa.Camera()

        # Set up the dashboard
        self.health_display = arcade.Text("", 20, self.height-30, font_size=20)
        self.items_collected = 0
        self.items_display = arcade.Text("", 200, self.height - 30, font_size=20)
        self.coin_sound_played = False
        
    def on_step(self):
        # Focus the world camera, and draw the scene
        self.world_camera.center_on_sprite(self.player, left_bound=0, lower_bound=0, right_bound=2000, upper_bound=2000)
        self.world_camera.use()
        self.clear()
        self.scene.draw()

        # Draw the grid - comment or remove this line when you no longer need the grid
        self.draw_grid()
        
        #draw the items collected display
        self.dashboard_camera.use()
        self.items_display.text = f"Items Collected: {self.items_collected}"
        self.items_display.draw()
        if self.items_collected == 6 and not self.coin_sound_played:
            hurt_SOUND = arcade.load_sound(get_asset_path("tada.wav",  subfolder="sounds"))
            self.coin_sound_played = True
            self.coin_playback = arcade.play_sound(hurt_SOUND)

        # Draw the dashboard
        self.dashboard_camera.use()
        self.health_display.text = f"Health: {self.player.health}"
        self.health_display.draw()


    def on_key_press(self, symbol, modifiers):
        
        if symbol == cc.Keys.B:
            Arrow(int(self.player.x), int(self.player.y))  
            
        if symbol == cc.Keys.SPACE: 
            err(int(self.player.x), int(self.player.y))     


