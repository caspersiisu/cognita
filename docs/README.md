# Cognita SDK Documentation

This document provides an extended guide for contributors, detailing the project setup, development workflow, usage examples, and best practices for contributing to the Cognita SDK project.

## Table of Contents

- [Project Overview](#project-overview)
- [Setup and Installation](#setup-and-installation)
- [Development Workflow](#development-workflow)
- [Usage Examples](#usage-examples)
- [Testing](#testing)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)
- [Contact](#contact)

## Project Overview

Cognita SDK is an AI-driven research workflow tool designed to facilitate automated knowledge discovery through interaction with the Deep Research API. The SDK is composed of several key modules:

- **Agent:** Manages research queries and workflows.
- **API Client:** Handles communication with the Deep Research API.
- **Configuration:** Centralizes configuration settings and environment variables.
- **Utilities:** Provides helper functions for query validation, response formatting, and result summarization.
- **Logging:** Implements consistent logging for debugging and monitoring.

## Setup and Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/caspersiisu/cognita.git
    cd cognita
    ```

2. **Create a Virtual Environment**

    It is recommended to use a virtual environment to manage dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**

    Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    pip install -e .
    ```

4. **Configure Environment Variables**

    Create a `.env` file in the project root with the following content:

    ```ini
    API_BASE_URL=https://api.research.com/v1
    API_KEY=your_api_key_here
    API_TIMEOUT=30
    MAX_RESULTS=10
    MIN_CONFIDENCE=0.7
    ```

## Development Workflow

To ensure a smooth development process, contributors should adhere to the following workflow:

1. **Fork the Repository**

   - Fork the repository on GitHub to your account.

2. **Create a Feature Branch**

   - Create a new branch for your feature or bugfix:

     ```bash
     git checkout -b feature/your-feature-name
     ```

3. **Make Changes and Commit**

   - Develop your changes locally.
   - Write clear and concise commit messages.
   - Ensure your changes follow the project's coding standards.

4. **Run Tests**

   - Before pushing changes, run the tests to ensure everything works as expected:

     ```bash
     pytest tests/
     ```

5. **Push Changes and Create a Pull Request**

   - Push your branch to your fork:

     ```bash
     git push origin feature/your-feature-name
     ```

   - Create a pull request against the main repository.

## Usage Examples

For a quick start, see the examples provided in the `examples/` directory:

- **quickstart.py:** A minimal example demonstrating how to initialize the agent, configure the API, and execute a basic research query.
- **research_query.py:** An advanced example showcasing a complete scientific research workflow using the agent.

## Testing

The project uses `pytest` as the testing framework. To run the test suite, execute:

```bash
pytest tests/
```

Ensure that your changes are covered by appropriate tests before submitting a pull request.

## Contribution Guidelines

Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for detailed instructions on how to contribute to the project, including coding standards, commit message guidelines, and pull request procedures.

## License

This project is licensed under the [MIT License](../LICENSE). See the LICENSE file for details.

## Contact

For any questions or further information, please refer to the project's GitHub repository for issue tracking and discussion.

---

Thank you for helping improve Cognita SDK!
