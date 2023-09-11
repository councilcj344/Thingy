```python
import numpy as np
from minecraft_ai.environment import Environment
from minecraft_ai.utils import log

class Agent:
    def __init__(self, config):
        self.config = config
        self.environment = Environment(config)
        self.state = None
        self.action_space = np.arange(self.environment.action_size)

    def get_state(self):
        self.state = self.environment.get_state()
        return self.state

    def select_action(self):
        action = np.random.choice(self.action_space)
        return action

    def update(self, action):
        next_state, reward, done = self.environment.step(action)
        self.state = next_state
        return reward, done

    def reset(self):
        self.state = self.environment.reset()

    def run(self):
        done = False
        total_reward = 0
        self.reset()
        while not done:
            action = self.select_action()
            reward, done = self.update(action)
            total_reward += reward
            log(f"Action: {action}, Reward: {reward}, Done: {done}")
        log(f"Total reward: {total_reward}")
```