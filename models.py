class Tile:
    def __init__(self, x, y):
        self.walkable = True
        self.x = x
        self.y = y

    def __str__(self):
        return "."


class Wall(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.walkable = False

    def __str__(self):
        return "#"


class NPC:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hostile = False

    def __str__(self):
        return "@"
