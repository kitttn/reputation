import curses
import pickle
from pickle import PickleError

from logic import Logic
from map import Map
from player import Player


class Game:
    def __init__(self, screen):
        if not self.load():
            height, width = screen.getmaxyx()
            self.map = Map(width - 1, height)
            self.player = Player()

        self.running = True
        self.logic = Logic(self.player, self.map)
        self.screen = screen
        self.run()

    def run(self):
        # self.screen.clear()
        self.render()

        while self.running:
            self.process_key()
            self.render()

        self.save()

    def render(self):
        self.map.render(self.screen)
        self.player.render(self.screen)
        self.screen.move(self.player.y, self.player.x)

    def process_key(self):
        key = self.screen.getkey()
        if key == 'q':
            self.running = False

        self.logic.key_pressed(key)

    def save(self):
        file = open('.save.world', 'wb')
        pickle.dump(self.map, file)
        file.close()

        file = open('.save.player', 'wb')
        pickle.dump(self.player, file)
        file.close()

    def load(self) -> bool:
        try:
            file = open('.save.world', 'rb')
            self.map = pickle.load(file)
            file = open('.save.player', 'rb')
            self.player = pickle.load(file)
            return True

        except PickleError:
            return False

        except FileNotFoundError:
            return False

        except EOFError:
            return False


curses.wrapper(Game)
