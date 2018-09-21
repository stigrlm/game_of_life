from game import Game
from inputs import InputHandler

input_handler = InputHandler()
game = Game(rounds =input_handler.args.rounds_number,
            world_size = input_handler.args.world_size,
            world_density = input_handler.args.live_density,
            rounds_per_sec = input_handler.args.run_speed)
game.run()
