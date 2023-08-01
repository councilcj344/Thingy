```python
import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""
    handler = logging.FileHandler(log_file)        
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def load_config(config_file):
    """Load configuration from a file"""
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Config file {config_file} not found.")
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

def save_state(state, file):
    """Save the current state of the game"""
    with open(file, 'w') as f:
        json.dump(state, f)

def load_state(file):
    """Load the saved state of the game"""
    if not os.path.exists(file):
        raise FileNotFoundError(f"State file {file} not found.")
    with open(file, 'r') as f:
        state = json.load(f)
    return state
```