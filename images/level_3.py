import op_arcade as oa
import op_arcade.constants_classes as cc

class Level_3(oa.View):

    def on_create(self):
        BRIDGE_TILE_WIDTH = 128 # For readability, we use a constant to specify the width of the bridge tile

        self.world_camera = oa.Camera() # Create a camera to allow for scrolling

        self.background_color = cc.Colors.AZURE
        self.player = Player(100, 200)

        # Add the bottom bridge platform (20 tiles in a row)
        for x in range(0, BRIDGE_TILE_WIDTH*20, BRIDGE_TILE_WIDTH):
            oa.Sprite(x, 20, ":resources:/images/tiles/bridgeA.png", cc.Layers.WALLS)

        # Add the upper bridge platform (1 tile only)
        oa.Sprite(800, 150, ":resources:/images/tiles/bridgeA.png", cc.Layers.WALLS)
        for i in range(87):
            oa.Sprite(900, 250, "images/duck.png")

    def on_step(self):
        # Make the camera follow the player
        self.world_camera.center_on_sprite(self.player, left_bound=0, lower_bound=-456789, right_bound=20000, upper_bound=88000)
        self.world_camera.use()

        self.clear()
        self.scene.draw()
        self.draw_grid()


class Player(oa.Sprite):

    def on_create(self):
        self.visual = "images/Windows_xp.jpg"
        self.scale = 0.6
        self.layer = cc.Layers.MOVING_GAME_OBJECTS
        self.bind_platformer_directional_keys() # Notice this time, we use the **platformer** directional keys
        self.enable_physics(gravity=0.01) #This is where we enable gravity for a platformer game


oa.run(Level_3)