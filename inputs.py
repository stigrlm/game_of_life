from argparse import ArgumentParser

class InputHandler(ArgumentParser):
    def __init__(self):
        super().__init__()

        self.add_argument('--world_size', help='Specify size of the world between 10-50.',
                            type=int, default=30)
        self.add_argument('--live_density', help='Specify proportion of alive cells at the beggining between 0-1',
                            type=float, default=0.5)
        self.add_argument('--rounds_number', help='Specify for how many rounds the game will run',
                            type=int, default=1000)
        self.add_argument('--run_speed', help='Specify how many roudns per second will be computed 4-20',
                            type=int, default=5)

        self.args = self.parse_args()

        if self.args.world_size not in range(10, 51):
            self.error("World size has to be between 10-50")
        if self.args.live_density < 0 or self.args.live_density > 1:
            self.error("Life density has to be between 0-1")
        if self.args.run_speed not in range(4, 31):
            self.error("Run speed has to be between 4-30")
