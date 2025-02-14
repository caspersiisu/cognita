# Cognita SDK

Cognita SDK is an AI-driven research workflow tool that empowers users to automate the discovery, synthesis, and summarization of scientific research. By interfacing with the Deep Research API, the SDK streamlines the process of gathering and processing research data.

## Features

- **AI Agent:** Seamlessly manage research queries and workflows.
- **API Integration:** Retrieve up-to-date research data via the Deep Research API.
- **Configuration Management:** Easily manage API settings with environment variables.
- **Utility Functions:** Validate queries, format API responses, and summarize research results.
- **Logging:** Integrated logging for robust debugging and monitoring.

## Installation

### Prerequisites

- Python 3.6 or above
- [pip](https://pip.pypa.io/en/stable/)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/caspersiisu/cognita.git
   cd cognita
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the Required Packages**

   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory with the following content:

   ```ini
   API_BASE_URL=https://api.research.com/v1
   API_KEY=your_api_key_here
   API_TIMEOUT=30
   MAX_RESULTS=10
   MIN_CONFIDENCE=0.7
   ```

## Usage Examples

### Quickstart

Below is a simple example to get you started quickly with Cognita SDK:

```python
from cognita import Config, CognitaAgent

def main():
    # Load configuration from environment variables
    config = Config()
    
    # Initialize the Cognita Agent
    agent = CognitaAgent(config)
    
    # Define a research query
    query = "Describe recent advancements in renewable energy technologies."
    
    # Execute the research query
    results = agent.execute_query(query)
    
    # Display the results
    print("Research Query Results:")
    print(results)

if __name__ == "__main__":
    main()
```

This example demonstrates how to initialize the SDK, execute a research query, and print the summarized results to the console.

### Advanced Research Workflow

For a more detailed example that demonstrates a complete scientific research workflow, refer to the `examples/quickstart.py` and `examples/research_query.py`file.

## Contribution Guidelines

We welcome contributions to Cognita SDK! If you’d like to contribute, please follow these steps:

- **Fork the Repository:** Create your own fork on GitHub.
- **Create a Feature Branch:** Use a descriptive name for your branch (e.g., `feature/new-ai-module` or `bugfix/fix-query-validation`).
- **Follow Coding Standards:** Adhere to [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines.
- **Write Tests:** Ensure your changes include tests and that all tests pass.
- **Submit a Pull Request:** Provide a clear description of your changes and reference any related issues.

For more detailed contribution guidelines, please see the [CONTRIBUTING.md](docs/CONTRIBUTING.md) document.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or further information, please refer to the project's GitHub repository for issue tracking and discussion.