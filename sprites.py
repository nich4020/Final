# Import external libraries
import arcade
import op_arcade as oa
import op_arcade.constants_classes as cc
from op_arcade import refs # refs gives us access to the current level
from arcade import Sound
import os 
def get_asset_path(filename, subfolder="images"):
        base = os.path.dirname(__file__)  # folder where your script lives
        return os.path.join(base, subfolder, filename)
class Player(oa.Sprite):
    SPEED = 4
    MAX_HEALTH = 10

    def on_create(self):
        # Set built-in attributes and called required methods
        self.visual = get_asset_path("duck.png")
        # cc.Anims.Players.TopDown.GIRL
        self.scale = 2
        self.set_layer(cc.Layers.MOVING_GAME_OBJECTS)
        self.bind_top_down_directional_keys(Player.SPEED)
        self.enable_physics()

        # Set our own custom attributes
        self.health = Player.MAX_HEALTH
        self.damage_immune = False # Will become True for a short period of time right after the player takes damage
        self.shoot_direction = "down" # When we shoot an arrow, which way does it go?

        

    def on_step(self):

        # Every time the player moves, we need to update its shoot direction.
        # Important to note, if we are currently stationary, there is no match below
        # and we stick with the most recent shoot direction
        if self.change_x > 0:
            self.shoot_direction = "right"
        elif self.change_x < 0:
            self.shoot_direction = "left"
        elif self.change_y < 0:
            self.shoot_direction = "down"
        elif self.change_y > 0:
            self.shoot_direction = "up"
            
        colliding_item = self.find_colliding("collectable")
        if colliding_item:
            self.view.items_collected += 1 # type: ignore
            colliding_item.kill()
            COIN_SOUND = arcade.load_sound(get_asset_path("ding.wav", subfolder="sounds"))
            arcade.play_sound(COIN_SOUND)


    # This method will be called by enemies when they give us damaage
    def take_damage(self, amount):
        if self.damage_immune: # abort if we are current immune to damage
            return

        self.health -= amount
        self.color = cc.Colors.RED
        self.damage_immune = True
        oa.set_timer(0.5, self.reset_damage_immunity)


    # this method gets called by the timer set in the take_damage method
    def reset_damage_immunity(self):
        self.color = cc.Colors.WHITE
        self.damage_immune = False


## BlueBird enemy
class BlueBird(oa.Sprite):
    SPEED = 5
    DISTANCE = 400 # How far will the bird fly before turning around?

    def on_create(self):
        # Set built-in attributes
        self.visual = "anims/blue_bird.yml"
        self.layer = cc.Layers.MOVING_GAME_OBJECTS
        self.change_x = BlueBird.SPEED

        # Set our own custom attributes
        self.left_bound = self.x
        self.right_bound = self.x + BlueBird.DISTANCE


    def on_step(self):
        # Turn around when we've reach our left bound
        if self.x < self.left_bound:
            self.change_x = BlueBird.SPEED
            self.scale_x = -1

        # Turn around when we've reach our right bound
        if self.x > self.right_bound:
            self.change_x = -BlueBird.SPEED
            self.scale_x = 1

        # If we're colliding with a player, give them damage
        colliding_player = self.find_colliding(Player)
        if colliding_player:
            colliding_player.take_damage(1)

        # If an arrow collides with us, remove ourself from the game
        if self.has_collision_with(Arrow):
            self.kill()

## Fly Enemy
class dog(oa.Sprite):
    SPEED = 3

    def on_create(self):
        # Set built-in attributes
        self.visual = get_asset_path("buddy.png")
        # cc.Images.Enemies.FLY
        self.layer = cc.Layers.MOVING_GAME_OBJECTS
        self.scale = 0.5

        # The fly has two possible states:
        #   "towards player" - default - move in to attack the player
        #   "retreat" - after it's hit the player - move up/left to give the player a moment
        self.movement_state = "towards player"

    def on_step(self):
        # This next line is a short form for:
        #
        #   if self.change_x > 0:
        #       self.scale_x = -0.5
        #   else:
        #       self.scale_x = 0.5
        # self.scale_x = -0.5 if self.change_x > 0 else 0.5
        
        if self.change_x > 0:
            if self.change_y > self.change_x:
                self.visual = get_asset_path("buddy_up.png")
            elif self.change_y < -self.change_x:    
                self.visual = get_asset_path("buddy_down.png")
            else:
                self.visual = get_asset_path("buddy.png")
    
        else:
            self.visual = get_asset_path("buddy_sit.png")              
        
        
        # Set the fly's movement according to its current state
        if self.movement_state == "towards player":
            self.move_towards_xy(self.view.player.x, self.view.player.y, dog.SPEED)
        elif self.movement_state == "retreat":
            self.change_x = -dog.SPEED
            self.change_y = dog.SPEED

        # Check if the fly has collided with the plyaer
        colliding_player = self.find_colliding(Player)
        if colliding_player:
            # colliding_player.take_damage(2)
            self.movement_state = "retreat"
            oa.set_timer(3, self.reset_movement_state)
        
        # Check if an arrow has collided with us
        if self.has_collision_with(bliss):
            self.kill()
        if self.has_collision_with(err):
            self.kill()
    # This is called by a timer - returns the fly to this state after it's
    # been in the retreat state for a period of time.
    def reset_movement_state(self):
        self.movement_state = "towards player"


class Coin (oa.Sprite):

    def on_create(self):
        # Set built-in attributes
        self.visual = cc.Anims.Items.GOLD_COIN
        self.layer = cc.Layers.STATIONARY_GAME_OBJECTS
        self.scale = 0.5
class buddy(oa.Sprite):
    def on_create(self):
        # Set built-in attributes
        self.visual = "images/buddy.png"
        self.layer = cc.Layers.MOVING_GAME_OBJECTS
        self.scale = 0.5

class bliss(oa.Sprite):
    SPEED = 10

    def on_create(self):
        # Set built-in attributes
        self.visual = "images/XP.png"
        self.layer = cc.Layers.MOVING_GAME_OBJECTS

        # Determine the value of the player's shoot_direction attribute and
        # copy it to a more convenient variable, dir
        dir = refs.cur_view.player.shoot_direction
        
        COIN_SOUND = arcade.load_sound("Local/Unit 4/part1/sounds/Windows XP Startup.wav")
        COIN_SOUND = arcade.play_sound(COIN_SOUND)
        # Set our speed and angle depending on the player's shoot_direction
        if dir == "right":
            self.change_x = Arrow.SPEED
        if dir == "left":
            self.change_x = -Arrow.SPEED
            self.angle = 180
        if dir == "up":
            self.change_y = Arrow.SPEED
            self.angle = 90
        if dir == "down":
            self.change_y = -Arrow.SPEED
            self.angle = 270
            
class err(oa.Sprite):
    SPEED = 10

    def on_create(self):
        # Set built-in attributes
        self.visual = "images/XP err.png"
        self.layer = cc.Layers.MOVING_GAME_OBJECTS

        # Determine the value of the player's shoot_direction attribute and
        # copy it to a more convenient variable, dir
        dir = refs.cur_view.player.shoot_direction
        
        err_SOUND = arcade.load_sound("Local/Unit 4/part1/sounds/chord.wav")
        err_SOUND = arcade.play_sound(err_SOUND)
        # Set our speed and angle depending on the player's shoot_direction
        if dir == "right":
            self.change_x = Arrow.SPEED
        if dir == "left":
            self.change_x = -Arrow.SPEED
            self.angle = 180
        if dir == "up":
            self.change_y = Arrow.SPEED
            self.angle = 90
        if dir == "down":
            self.change_y = -Arrow.SPEED
            self.angle = 270
class vista_orb(oa.Sprite):

    def on_create(self):
        Windowsvista = "images/Windows_Vista.jpg" 
        self.visual = Windowsvista
        self.scale = 0.5
        self.layer = cc.Layers.MOVING_GAME_OBJECTS
        self.change_x = 8
        vista_orb_sOUND = arcade.load_sound("Local/Unit 4/part1/sounds/Windows Shutdown.wav")
        vista_orb_play = arcade.play_sound(vista_orb_sOUND)


    def on_step(self):
        # If we've gone off screen, remove ourself from the game.
        # It's important to remember this step, or otherwise the game will eventually
        # slow down and it's trying to render a bunch of arrows off screen
        if self.x == 1600:
            self.kill() 
        # # refs.cur_view.world_camera.point_in_view(int(self.x), int(self.y)) == False:
        #     self.kill()
