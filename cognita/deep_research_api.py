"""
Deep Research API Handler for Cognita SDK

This module manages interactions with the Deep Research API, allowing the Cognita agent 
to retrieve scientific research data.

Features:
- Handles research queries and sends them to the Deep Research API.
- Manages API authentication using API keys.
- Implements error handling for failed API requests.
- Uses logging for better debugging and monitoring.
"""

import requests
import logging
from typing import Dict, Any
from .config import Config
from .errors import APIError

class DeepResearchAPI:
    """Handler for Deep Research API interactions."""
    
    def __init__(self, config: Config):
        """
        Initialize the API client with the provided configuration.

        Args:
            config (Config): Configuration object containing API details.
        """
        self.config = config  # Store the configuration instance
        self.base_url = config.API_BASE_URL
        self.api_key = config.API_KEY
        self.timeout = config.API_TIMEOUT
        self.logger = logging.getLogger(__name__)

    def submit_research_request(self, query: str) -> Dict[str, Any]:
        """
        Submit a research request to the Deep Research API.

        Args:
            query (str): Validated research query.

        Returns:
            dict: Raw API response containing research data.

        Raises:
            APIError: If there are issues with API communication or response handling.
        """
        endpoint = f"{self.base_url}/research"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "query": query,
            "parameters": {
                "max_results": self.config.MAX_RESULTS,
                "min_confidence": self.config.MIN_CONFIDENCE
            }
        }

        try:
            response = requests.post(
                endpoint,
                json=payload,
                headers=headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"API Request Failed: {str(e)}")
            raise APIError(f"API communication error: {str(e)}")
