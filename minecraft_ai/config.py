```python
# minecraft_ai/config.py

# Configuration settings for the Minecraft AI

# Game settings
GAME_SETTINGS = {
    'world_name': 'AI World',
    'difficulty': 'normal',
    'game_mode': 'survival',
}

# Agent settings
AGENT_SETTINGS = {
    'name': 'AI Agent',
    'strategy': 'exploration',
}

# Logging settings
LOGGING_SETTINGS = {
    'log_level': 'info',
    'log_file': 'minecraft_ai.log',
}

def get_game_settings():
    return GAME_SETTINGS

def get_agent_settings():
    return AGENT_SETTINGS

def get_logging_settings():
    return LOGGING_SETTINGS
```