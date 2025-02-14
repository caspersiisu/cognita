import os
from dotenv import load_dotenv

class Config:
    """
    Central configuration management class for Cognita SDK.

    This class loads configuration settings from environment variables 
    and provides a structured way to access them.

    Features:
    - Loads environment variables using `dotenv`.
    - Provides default values for optional settings.
    - Validates essential configuration parameters.

    Attributes:
        API_BASE_URL (str): Base URL for the Deep Research API.
        API_KEY (str): API key for authentication.
        API_TIMEOUT (int): Timeout duration for API requests.
        MAX_RESULTS (int): Maximum number of research results per request.
        MIN_CONFIDENCE (float): Minimum confidence score for filtering research results.
    """

    def __init__(self):
        """Initialize configuration from environment variables."""
        load_dotenv()
        
        # API Configuration
        self.API_BASE_URL = os.getenv("API_BASE_URL", "https://api.research.com/v1")
        self.API_KEY = os.getenv("API_KEY")
        self.API_TIMEOUT = int(os.getenv("API_TIMEOUT", 30))
        self.MAX_RESULTS = int(os.getenv("MAX_RESULTS", 10))
        self.MIN_CONFIDENCE = float(os.getenv("MIN_CONFIDENCE", 0.7))
        
        # Validate required settings
        if not self.API_KEY:
            raise ValueError("API_KEY must be set in environment variables")
