from world import World
from datetime import datetime
from time import sleep

class Game:
    def __init__(self, rounds, world_size, world_density, rounds_per_sec):
        self.rounds = rounds
        self.world = World(world_size, world_density)
        self.round_num = 0
        self.game_speed = 1/rounds_per_sec

    def run(self):
        for i in range(self.rounds+1):
            self.run_round()

    def run_round(self):
        # runs one round of game
        start = datetime.now()
        self.world.display_world()
        print("Round: {}".format(self.round_num))
        self.world.resolve_cells()
        self.world.update_round()
        self.round_num += 1
        duration = datetime.now() - start
        sleep_time = self.game_speed - duration.total_seconds()
        if sleep_time > 0:
            sleep(sleep_time)
