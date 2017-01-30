import random

from models import Wall, Tile


class Map:
    def __init__(self, width, height):
        self.indent = "== "
        self.width = width
        self.height = height
        self._world = [[Tile(x, y) for x in range(width)] for y in range(height)]

        self.curr_x = 1
        self.curr_y = 1

        self.start_x = self.curr_x
        self.start_y = self.curr_y

        self.generate_world(width, height)
        # self.generate_labyrinth(0, 0, width, height, 1)

    def generate_world(self, width, height):
        """
        This generates simple squared map to walk on
        """
        for _ in range(width):
            self._world[0][_] = Wall(0, _)
            self._world[height - 1][_] = Wall(height - 1, _)

        for _ in range(height):
            self._world[_][0] = Wall(_, 0)
            self._world[_][width - 1] = Wall(_, width - 1)

    def generate_labyrinth(self, curr_x, curr_y, width, height, level) -> bool:
        """
        This generates labyrinth
        """

        pairs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        random.shuffle(pairs)

        dx = [x[0] for x in pairs]
        dy = [y[1] for y in pairs]

        for l in range(4):
            x = dx[l] + curr_x
            y = dy[l] + curr_y
            if x == self.start_x and y == self.start_y:
                return True

            # if not (corr_x <= x < width + corr_x and corr_y <= y < height + corr_y):
            if self.check_neighbors(curr_x, curr_y, x, y, level):
                print("%sSelected (%d, %d)!" % (self.indent * level, x, y))
                self._world[y][x] = Wall(x, y)
                self.generate_labyrinth(x, y, width, height, level + 1)
            else:
                print("%sNot working, trying another..." % (self.indent * level))

    def check_neighbors(self, prev_x, prev_y, cur_x, cur_y, level) -> bool:
        print("%sChecking way (%d, %d) -> (%d, %d)" % (
            self.indent * level, prev_x, prev_y, cur_x, cur_y))

        can_walk = False
        check_cells = [(x, y)
                       for x in range(cur_x - 1, cur_x + 2)
                       for y in range(cur_y - 1, cur_y + 2)]

        # print(check_cells)

        def predicate(pair):
            return ((prev_x - cur_x == 0 and prev_y - cur_y == 0) or
                    (prev_x - cur_x != 0 and pair[0] != prev_x) or
                    (prev_y - cur_y != 0 and pair[1] != prev_y)) and \
                   (pair[0] != cur_x or pair[1] != cur_y)

        check_cells = [pair for pair in check_cells if predicate(pair)]

        has_walls = False
        # filtering that no walls are there
        for pair in check_cells:
            x, y = pair
            if self.in_range(x, y) and self._world[y][x] == '#':
                has_walls = True

        if self.in_range(cur_x, cur_y):
            can_walk = True

        return can_walk and not has_walls

    def get_tile(self, x, y) -> Tile:
        return self._world[y][x]

    def in_range(self, x, y) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, screen):
        for i in range(self.height):
            line = "".join([str(x) for x in self._world[i]])
            screen.addstr(i, 0, line)
