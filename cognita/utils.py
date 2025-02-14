"""
Utility Module for Cognita SDK

This module provides helper functions for validating user queries,
formatting API responses, and summarizing results.

Features:
- Query validation to ensure meaningful research queries.
- Response formatting for standardizing API results.
- Summarization function for processing final results.
"""

from typing import Dict, Any
from .errors import ProcessingError

def validate_query(query: str) -> str:
    """
    Validate and sanitize research query.
    
    Ensures the query meets minimum length requirements and removes unnecessary whitespace.
    
    Args:
        query (str): Raw input query
        
    Returns:
        str: Sanitized query
        
    Raises:
        ProcessingError: If the query is too short (less than 10 characters)
    """
    cleaned = query.strip()
    if len(cleaned) < 10:
        raise ProcessingError("Query too short (min 10 characters)")
    return cleaned

def format_response(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Standardize API response format.
    
    Extracts key information from the API response and ensures consistency in data representation.
    
    Args:
        raw_data (dict): Raw API response containing research results
        
    Returns:
        dict: Structured research results including summary, sources, and confidence score
        
    Raises:
        ProcessingError: If the response format is invalid or missing expected fields
    """
    try:
        return {
            "summary": raw_data.get("summary", ""),
            "sources": raw_data.get("sources", []),
            "confidence": raw_data.get("confidence_score", 0.0)
        }
    except AttributeError as e:
        raise ProcessingError(f"Invalid response format: {str(e)}")

def summarize_results(results: Dict[str, Any]) -> Dict[str, Any]:
    """
    Summarize the research results for easier consumption.

    For this minimal example, we simply wrap the existing results in a
    new dictionary, but you can extend this to perform more complex
    summarization logic (e.g., extracting key points, generating
    short paragraphs, etc.).

    Args:
        results (dict): The formatted research results, containing
                        'summary', 'sources', and 'confidence' keys.

    Returns:
        dict: A dictionary with a 'final_summary' plus any other data you want to include.
    """
    return {
        "final_summary": results.get("summary", "No summary available"),
        "sources": results.get("sources", []),
        "confidence": results.get("confidence", 0.0)
    }
