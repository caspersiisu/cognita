# Cognita SDK API Reference

Welcome to the Cognita SDK API Reference. This document provides an in-depth overview of all public modules, classes, and functions available in the SDK. It is intended to serve as a guide for developers looking to integrate, extend, or contribute to the project.

---

## Table of Contents

- [Overview](#overview)
- [Modules](#modules)
  - [agent](#agent)
  - [config](#config)
  - [deep_research_api](#deep_research_api)
  - [errors](#errors)
  - [logging_config](#logging_config)
  - [utils](#utils)
- [Getting Started](#getting-started)
- [Examples](#examples)
- [Additional Resources](#additional-resources)

---

## Overview

The Cognita SDK provides an AI-driven research workflow for automated knowledge discovery. It is composed of several interconnected modules that manage everything from API communications to data processing and logging. Below is an outline of the primary components:

- **Agent**: Coordinates research queries and workflow management.
- **Config**: Centralizes all configuration settings.
- **Deep Research API**: Handles communication with the external research API.
- **Errors**: Contains custom exceptions for error handling.
- **Logging**: Sets up and configures standardized logging.
- **Utils**: Offers helper functions for query validation, response formatting, and summarization.

---

## Modules

### 1. cognita/agent.py

**Module Path:** `cognita.agent`

The `agent` module is responsible for managing research workflows. It defines the `CognitaAgent` class, which encapsulates the entire process of validating input, interacting with the API, formatting responses, and summarizing results.

#### `CognitaAgent` Class

- **Description:**  
  The primary interface for executing research queries. It integrates all necessary components—configuration, API communication, utilities, and logging—to deliver processed research results.

- **Constructor:**  
  `__init__(self, config)`  
  **Parameters:**
  - `config` (*Config*): An instance of the configuration class containing API settings.  
  **Behavior:**  
  Initializes the agent, sets up the `DeepResearchAPI` instance, and configures logging.

- **Methods:**

  - `execute_query(self, query: str) -> Dict[str, Any]`  
    **Parameters:**
    - `query` (*str*): A research question or topic.
    
    **Returns:**  
    - A dictionary with the structured and summarized research results.
    
    **Raises:**  
    - `APIError`: If communication with the API fails.
    - `ProcessingError`: If there is an error during data processing.
    
    **Description:**  
    This method validates the query, sends it to the Deep Research API, formats the response, and produces a final summary.
    
  - `summarize_results(self, results: Dict[str, Any]) -> Dict[str, Any]`  
    **Parameters:**
    - `results` (*dict*): Formatted research results.
    
    **Returns:**  
    - A dictionary containing the final summarized results.
    
    **Description:**  
    Uses utility functions to generate a concise summary of the research data for easier consumption.

---

### 2. cognita/config.py

**Module Path:** `cognita.config`

The `config` module is responsible for loading and managing configuration parameters for the SDK. It leverages environment variables (using `python-dotenv`) to initialize API settings.

#### `Config` Class

- **Description:**  
  Loads configuration settings from the environment and provides default values for optional parameters. It ensures that essential settings, like the API key, are available.

- **Attributes:**
  - `API_BASE_URL` (*str*): Base URL of the Deep Research API.
  - `API_KEY` (*str*): API key used for authentication.
  - `API_TIMEOUT` (*int*): Timeout for API requests.
  - `MAX_RESULTS` (*int*): Maximum number of results per API call.
  - `MIN_CONFIDENCE` (*float*): Minimum confidence threshold for the results.

- **Constructor:**  
  `__init__(self)`  
  **Behavior:**  
  Reads environment variables, applies default values, and validates the presence of required settings (raising a `ValueError` if the API key is missing).

---

### 3. cognita/deep_research_api.py

**Module Path:** `cognita.deep_research_api`

This module encapsulates the communication with the Deep Research API. It handles request formation, sending data over HTTP, and error management.

#### `DeepResearchAPI` Class

- **Description:**  
  Manages the submission of research queries to the Deep Research API, including building the request payload and handling API responses.

- **Constructor:**  
  `__init__(self, config: Config)`  
  **Parameters:**
  - `config` (*Config*): The configuration object containing API details.
  
  **Behavior:**  
  Stores the configuration and initializes logging for API interactions.

- **Methods:**

  - `submit_research_request(self, query: str) -> Dict[str, Any]`  
    **Parameters:**
    - `query` (*str*): A validated research query.
    
    **Returns:**  
    - A dictionary representing the raw JSON response from the API.
    
    **Raises:**  
    - `APIError`: If the API call fails (e.g., network error, invalid response).
    
    **Description:**  
    Constructs the API endpoint, headers, and payload (using configuration parameters for `max_results` and `min_confidence`), and sends an HTTP POST request to the API. If the API responds with an error, the method logs the error and raises an `APIError`.

---

### 4. cognita/errors.py

**Module Path:** `cognita.errors`

This module defines custom exceptions used throughout the Cognita SDK to provide clear and consistent error reporting.

#### Exceptions

- **`APIError`**  
  **Description:**  
  Raised when there is an error during API communication (e.g., failed request, timeout).
  
  **Usage:**  
  Typically raised in `DeepResearchAPI.submit_research_request`.

- **`ConfigError`**  
  **Description:**  
  Raised for configuration-related issues, such as missing or invalid settings.
  
- **`ProcessingError`**  
  **Description:**  
  Raised when an error occurs during data processing, such as query validation failures or response formatting issues.

---

### 5. cognita/logging_config.py

**Module Path:** `cognita.logging_config`

This module sets up a standardized logging configuration for the SDK.

- **Description:**  
  Configures the logging system to write logs to both a file (`cognita.log`) and the console. It defines the log format, log level, and handlers.
  
- **Usage:**  
  Importing this module initializes logging for the entire application. No public classes or functions are exposed, but it is essential for debugging and monitoring.

---

### 6. cognita/utils.py

**Module Path:** `cognita.utils`

The `utils` module contains helper functions used across the SDK for tasks such as query validation, response formatting, and result summarization.

#### Functions

- **`validate_query(query: str) -> str`**  
  **Description:**  
  Sanitizes and validates a research query. Ensures that the query meets a minimum length requirement.
  
  **Parameters:**
  - `query` (*str*): The raw input query.
  
  **Returns:**  
  - A sanitized version of the query.
  
  **Raises:**  
  - `ProcessingError`: If the query is too short.

- **`format_response(raw_data: Dict[str, Any]) -> Dict[str, Any]`**  
  **Description:**  
  Standardizes the format of the API response by extracting key information such as summary, sources, and confidence score.
  
  **Parameters:**
  - `raw_data` (*dict*): The raw JSON response from the API.
  
  **Returns:**  
  - A formatted dictionary of research results.
  
  **Raises:**  
  - `ProcessingError`: If the response is not in the expected format.

- **`summarize_results(results: Dict[str, Any]) -> Dict[str, Any]`**  
  **Description:**  
  Provides a final summary of the research results. This function can be extended to include advanced summarization logic.
  
  **Parameters:**
  - `results` (*dict*): Formatted research results.
  
  **Returns:**  
  - A dictionary containing a final summary and other key result details.

---

## Getting Started

To begin using the Cognita SDK in your project, import the main classes and initialize them with a valid configuration:

```python
from cognita import CognitaAgent, Config

# Initialize configuration from environment variables
config = Config()

# Create an instance of CognitaAgent
agent = CognitaAgent(config)

# Execute a research query
query = "What are the recent trends in renewable energy?"
results = agent.execute_query(query)
print(results)
```

---

## Examples

For practical usage examples, refer to the following files in the `examples/` directory:
- **quickstart.py**: A minimal example demonstrating basic initialization and query execution.
- **research_query.py**: An advanced example showcasing a complete research workflow.

---

## Additional Resources

- **Project Repository:**  
  Visit the [GitHub Repository](https://github.com/caspersiisu/cognita) for the source code and further documentation.
- **Testing:**  
  The test suite is located in the `tests/` directory. Run tests with:
  ```bash
  pytest tests/
  ```
- **Contribution Guidelines:**  
  For instructions on contributing, see the [CONTRIBUTING.md](CONTRIBUTING.md) file.

---

This API Reference is intended to be a living document that evolves as the Cognita SDK grows. Please refer back to it for the most up-to-date information on the SDK's functionality.

