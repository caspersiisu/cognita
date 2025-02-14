# Contributing to Cognita SDK

Thank you for considering contributing to Cognita SDK! We welcome your help in making this project better for everyone. Whether you’re reporting a bug, suggesting a new feature, or submitting a pull request, your contributions are appreciated.

## Table of Contents

- [How to Contribute](#how-to-contribute)
- [Code Style Guidelines](#code-style-guidelines)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Branching and Pull Requests](#branching-and-pull-requests)
- [Testing](#testing)
- [Reporting Issues](#reporting-issues)
- [Additional Resources](#additional-resources)
- [Contact](#contact)

## How to Contribute

There are several ways you can contribute to Cognita SDK:

- **Bug Reports:** If you encounter any issues, please open a GitHub issue with clear steps to reproduce the problem.
- **Feature Requests:** If you have an idea for an improvement or a new feature, open an issue to discuss it before starting development.
- **Code Contributions:** Fork the repository, implement your changes, and submit a pull request (PR). Ensure your code adheres to our guidelines.
- **Documentation:** Improvements to documentation, examples, and API references are always welcome.
- **Testing:** Write tests for new features or bug fixes, and ensure all tests pass before submitting your PR.

## Code Style Guidelines

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) as our style guide for Python code. Here are some key points:

- **Indentation:** Use 4 spaces per indentation level.
- **Line Length:** Limit lines to 79 characters.
- **Naming:** Use meaningful and descriptive names for variables, functions, and classes.
- **Docstrings:** Provide clear docstrings for all public modules, classes, and functions.
- **Comments:** Write comments to explain non-obvious parts of the code.

Please run a linter (e.g., `flake8`) locally to check your code style before submitting your PR.

## Commit Message Guidelines

Good commit messages help others understand the history of changes. Please follow these guidelines:

- **Tense:** Use the present tense ("Add feature", "Fix bug") rather than past tense.
- **Capitalization:** Capitalize the first letter of the subject line.
- **Punctuation:** Do not end the subject line with a period.
- **Separation:** Separate the subject from the body with a blank line.
- **Content:** Include a brief summary in the subject, and more detailed information in the body if necessary.

Example commit message:

```
Add support for multi-language queries

This commit introduces a new feature to support queries in multiple languages.
It includes updates to the API handling and new unit tests.
```

## Branching and Pull Requests

1. **Fork the Repository:** Create a fork of the repository on GitHub.
2. **Create a Feature Branch:** Create a new branch for your work with a descriptive name (e.g., `feature/multi-language-support` or `bugfix/fix-query-validation`).
3. **Commit Your Changes:** Commit your changes locally following the commit guidelines.
4. **Push Your Branch:** Push your branch to your fork.
5. **Submit a Pull Request:** Open a pull request against the `main` branch of the upstream repository. Provide a clear description of your changes and reference any related issues.

## Testing

- **Write Tests:** Ensure that your changes include new tests or update existing ones as needed.
- **Run Tests:** Execute the test suite locally to ensure that all tests pass:
  
  ```bash
  pytest tests/
  ```
  
- **Coverage:** Aim for high test coverage for new features and bug fixes.

## Reporting Issues

If you discover a bug or have suggestions for improvements, please open an issue on GitHub. When reporting issues, include:
- A clear description of the problem.
- Steps to reproduce the issue.
- Expected behavior vs. actual behavior.
- Any relevant logs, screenshots, or error messages.

## Additional Resources

- [Project README](../README.md) – Overview of the project and basic setup instructions.
- [API Reference](API_REFERENCE.md) – Detailed documentation of the public modules, classes, and functions.
## Contact

If you have any questions or need further assistance, please feel free to reach out via GitHub issues or contact me.

Thank you for contributing to Cognita SDK!
