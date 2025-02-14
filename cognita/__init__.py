"""
Cognita SDK

This package provides an AI-driven research workflow, allowing users to interact 
with the Deep Research API for automated knowledge discovery.

Modules:
    - agent: Core AI agent for managing research workflows.
    - config: Configuration management for API settings.
    - deep_research_api: API client for interacting with the Deep Research API.

Exports:
    - CognitaAgent: Main interface for executing research queries.
    - Config: Configuration manager for environment settings.
    - DeepResearchAPI: API handler for submitting research requests.

Version:
    0.0.1
"""

from .agent import CognitaAgent
from .config import Config
from .deep_research_api import DeepResearchAPI

__all__ = ['CognitaAgent', 'Config', 'DeepResearchAPI']
__version__ = '0.0.1'
