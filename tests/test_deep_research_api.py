import pytest
import requests
from cognita.deep_research_api import DeepResearchAPI
from cognita.errors import APIError

# Dummy configuration object for testing
class DummyConfig:
    API_BASE_URL = "http://dummyapi.com"
    API_KEY = "dummykey"
    API_TIMEOUT = 10
    MAX_RESULTS = 5
    MIN_CONFIDENCE = 0.8

# Helper class to simulate responses from requests.post
class FakeResponse:
    def __init__(self, json_data, status_code=200):
        self._json_data = json_data
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.exceptions.HTTPError(f"HTTP error: {self.status_code}")

    def json(self):
        return self._json_data

def test_submit_research_request_success(monkeypatch):
    """
    Test that submit_research_request returns the correct response when the API call is successful.
    """
    config = DummyConfig()
    api_client = DeepResearchAPI(config)
    
    def fake_post(url, json, headers, timeout):
        return FakeResponse({
            "summary": "Fake summary",
            "sources": ["Fake Source"],
            "confidence_score": 0.9
        }, status_code=200)
    
    monkeypatch.setattr(requests, "post", fake_post)
    result = api_client.submit_research_request("A valid research query?")
    expected = {
        "summary": "Fake summary",
        "sources": ["Fake Source"],
        "confidence_score": 0.9
    }
    assert result == expected

def test_submit_research_request_failure(monkeypatch):
    """
    Test that submit_research_request raises an APIError when a communication error occurs.
    """
    config = DummyConfig()
    api_client = DeepResearchAPI(config)
    
    def fake_post(url, json, headers, timeout):
        raise requests.exceptions.RequestException("Simulated network error")
    
    monkeypatch.setattr(requests, "post", fake_post)
    with pytest.raises(APIError):
        api_client.submit_research_request("A valid research query?")
