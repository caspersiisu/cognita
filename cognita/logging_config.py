# logging_config.py
"""
Logging Configuration Module

This module sets up a standardized logging configuration for the Cognita SDK.
It ensures that logs are recorded in both a log file and the console,
making debugging and monitoring easier.

Features:
- Logs are saved to `cognita.log`.
- Logs are displayed in the console for real-time monitoring.
- Log format includes timestamp, log level, and message.
- Supports INFO level logging by default.
"""

import logging

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,  # Set log level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    handlers=[
        logging.FileHandler("cognita.log"),  # Save logs to a file
        logging.StreamHandler()  # Print logs to console
    ]
)

# Create a logger instance
logger = logging.getLogger("CognitaSDK")

# Example log messages (for testing purposes)
if __name__ == "__main__":
    logger.info("Logging system initialized.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
