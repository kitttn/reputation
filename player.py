class Player:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.image = '@'

    def render(self, screen):
        screen.addstr(self.y, self.x, self.image)
        screen.move(self.y, self.x)
