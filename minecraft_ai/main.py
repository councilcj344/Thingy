```python
import logging
from minecraft_ai import agent, environment, utils, config

def main():
    # Initialize logging
    logging.basicConfig(level=logging.INFO)

    # Load configuration settings
    settings = config.load_settings()

    # Initialize the game environment
    env = environment.MinecraftEnvironment(settings)

    # Initialize the AI agent
    ai_agent = agent.MinecraftAgent(env, settings)

    # Main game loop
    while True:
        # Update the game state
        game_state = env.update_state()

        # Let the AI agent take an action based on the current game state
        ai_agent.take_action(game_state)

        # Check if the game is over
        if env.is_game_over():
            logging.info("Game over.")
            break

if __name__ == "__main__":
    main()
```