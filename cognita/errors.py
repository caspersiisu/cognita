"""
Custom Exception Module for Cognita SDK

This module defines custom exceptions to handle errors more effectively within the Cognita SDK.

Features:
- `APIError`: Raised for API-related issues (e.g., failed requests, invalid responses).
- `ConfigError`: Raised when configuration issues occur (e.g., missing API keys, incorrect settings).
- `ProcessingError`: Raised for issues during data processing (e.g., invalid input data, parsing failures).
"""

class APIError(Exception):
    """Exception raised for API-related errors."""
    def __init__(self, message: str):
        super().__init__(f"API Error: {message}")

class ConfigError(Exception):
    """Exception raised for configuration errors."""
    def __init__(self, message: str):
        super().__init__(f"Configuration Error: {message}")

class ProcessingError(Exception):
    """Exception raised during data processing."""
    def __init__(self, message: str):
        super().__init__(f"Processing Error: {message}")