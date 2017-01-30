import curses


class Logic:
    def __init__(self, player, map):
        self.player = player
        self.map = map

        self.logger = open('logic.log', 'w')

    def key_pressed(self, key):
        x = self.player.x
        y = self.player.y
        moved = False

        new_x, new_y = x, y

        if key == "KEY_LEFT":
            new_x = x - 1
            moved = True

        if key == "KEY_RIGHT":
            new_x = x + 1
            moved = True

        if key == "KEY_UP":
            new_y = y - 1
            moved = True

        if key == "KEY_DOWN":
            new_y = y + 1
            moved = True

        self.logger.write("===\nKey: %s\n" % key)
        self.logger.write("In range: %s, walkable: %s\n" % (self.map.in_range(new_x, new_y), self.map.get_tile(new_x, new_y)))
        if self.map.in_range(new_x, new_y) and self.map.get_tile(new_x, new_y).walkable and moved:
            self.player.x = new_x
            self.player.y = new_y
            self.logger.write("Moved to (%d, %d)\n" % (new_x, new_y))