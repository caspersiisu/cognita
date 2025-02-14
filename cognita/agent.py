import logging
from typing import Dict, Any
from .deep_research_api import DeepResearchAPI
from .utils import format_response, validate_query, summarize_results
from .errors import APIError, ProcessingError

class CognitaAgent:
    """
    Core AI agent for managing research workflows in the Cognita SDK.

    This class acts as the main interface for executing research queries, interacting 
    with the Deep Research API, processing responses, and summarizing results.

    Attributes:
        config (Config): Configuration object containing API settings.
        api (DeepResearchAPI): API handler for making research requests.
        logger (logging.Logger): Logger instance for tracking operations and errors.
    """

    def __init__(self, config):
        """
        Initialize the research agent with configuration settings.

        Args:
            config (Config): Configuration object with API settings.
        """
        self.config = config
        self.api = DeepResearchAPI(config)
        self.logger = logging.getLogger(__name__)
        self.logger.info("Cognita Agent initialized with configuration: %s", config)

    def execute_query(self, query: str) -> Dict[str, Any]:
        """
        Execute a research query and process the results.

        This method validates the input query, submits it to the Deep Research API, 
        formats the response, and summarizes the research findings.

        Args:
            query (str): Research question or topic.

        Returns:
            dict: Structured and summarized research results.

        Raises:
            APIError: Raised if an error occurs while communicating with the API.
            ProcessingError: Raised if there is an issue with processing the research data.
        """
        try:
            validated = validate_query(query)
            self.logger.debug("Validated query: %s", validated)
            
            raw_response = self.api.submit_research_request(validated)
            self.logger.debug("Raw response received: %s", raw_response)
            
            formatted_response = format_response(raw_response)
            self.logger.debug("Formatted response: %s", formatted_response)
            
            summarized_results = self.summarize_results(formatted_response)
            self.logger.debug("Summarized results: %s", summarized_results)
            
            return summarized_results
        
        except APIError as e:
            self.logger.error(f"API Error: {str(e)}")
            raise
        except ProcessingError as e:
            self.logger.error(f"Processing Error: {str(e)}")
            raise

    def summarize_results(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Summarize the research results for easier consumption.

        This method extracts key information from the research results to 
        provide a concise summary.

        Args:
            results (dict): The formatted research results.

        Returns:
            dict: Summarized research results.

        Raises:
            ProcessingError: Raised if an error occurs while summarizing the results.
        """
        try:
            summary = summarize_results(results)
            self.logger.info("Results summarized successfully")
            return summary
        except Exception as e:
            self.logger.error(f"Error summarizing results: {str(e)}")
            raise ProcessingError("Failed to summarize results") from e
