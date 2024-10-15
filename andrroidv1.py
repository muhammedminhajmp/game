import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty
from kivy.clock import Clock
from kivy.core.window import Window

# Set window size for testing on desktop (for mobile, this will adjust automatically)
Window.size = (800, 600)

# Player class
class Player(Widget):
    velocity_y = NumericProperty(0)  # Jump/fall speed

    def move(self):
        # Gravity effect
        self.velocity_y -= 0.5
        self.y += self.velocity_y

        # Stop player from falling below the ground
        if self.y < 0:
            self.y = 0
            self.velocity_y = 0

    def jump(self):
        if self.y == 0:  # Jump only if player is on the ground
            self.velocity_y = 15

# Game world class
class PlatformerGame(Widget):
    player = ObjectProperty(None)  # Use ObjectProperty for the player widget

    def __init__(self, **kwargs):
        super(PlatformerGame, self).__init__(**kwargs)
        # Add player instance
        self.player = Player(size=(50, 50), pos=(100, 100))
        self.add_widget(self.player)
        
        # Add a basic platform
        self.platform = Widget(size=(400, 20), pos=(100, 50))
        self.add_widget(self.platform)
        
        # Schedule the update function to be called every frame
        Clock.schedule_interval(self.update, 1.0 / 60.0)  # Call update at 60 FPS

    def update(self, dt):
        # Call player movement
        self.player.move()

        # Check for collision with platform (basic collision detection)
        if self.player.collide_widget(self.platform):
            self.player.velocity_y = 0
            self.player.y = self.platform.top

    def on_touch_down(self, touch):
        # Jump when the screen is touched
        self.player.jump()

# Kivy App class
class PlatformerApp(App):
    def build(self):
        game = PlatformerGame()
        return game

if __name__ == '__main__':
    PlatformerApp().run()
