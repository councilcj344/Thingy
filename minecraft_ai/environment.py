```python
import numpy as np
from minecraft_ai import utils, config

class Environment:
    def __init__(self):
        self.state = None
        self.config = config.load_config()

    def reset(self):
        self.state = np.zeros((self.config['world_size'], self.config['world_size'], self.config['world_size']))

    def update_state(self, new_state):
        self.state = new_state

    def get_state(self):
        return self.state

    def is_valid_move(self, move):
        # Check if the move is within the bounds of the world
        return 0 <= move[0] < self.config['world_size'] and 0 <= move[1] < self.config['world_size'] and 0 <= move[2] < self.config['world_size']

    def apply_move(self, move):
        if self.is_valid_move(move):
            self.state[move[0]][move[1]][move[2]] = 1
        else:
            raise ValueError("Invalid move")

    def get_possible_moves(self):
        possible_moves = []
        for x in range(self.config['world_size']):
            for y in range(self.config['world_size']):
                for z in range(self.config['world_size']):
                    if self.state[x][y][z] == 0:
                        possible_moves.append((x, y, z))
        return possible_moves
```