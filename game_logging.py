import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Create a logger
logger = logging.getLogger('dxball')
logger.setLevel(logging.INFO)

# Create formatters
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Create file handler
log_file = f'logs/game_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def log_powerups(allowed_powerups):
    """Log the allowed powerups for the current level."""
    logger.info("Allowed powerups for this level:")
    for powerup in allowed_powerups:
        logger.info(f"- {powerup}") 