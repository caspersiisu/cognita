import pytest
from cognita.agent import CognitaAgent
from cognita.errors import ProcessingError

# Dummy configuration object for testing
class DummyConfig:
    API_BASE_URL = "http://dummyapi.com"
    API_KEY = "dummykey"
    API_TIMEOUT = 10
    MAX_RESULTS = 5
    MIN_CONFIDENCE = 0.8

@pytest.fixture
def dummy_agent(monkeypatch):
    """
    Fixture to create a CognitaAgent instance with monkeypatched dependencies.
    """
    config = DummyConfig()
    agent = CognitaAgent(config)
    
    # Override the API call to avoid real HTTP requests
    def fake_submit_research_request(query: str):
        # Simulated raw response from the API
        return {
            "summary": "Test summary",
            "sources": ["Test Source"],
            "confidence_score": 0.99
        }
    monkeypatch.setattr(agent.api, "submit_research_request", fake_submit_research_request)
    
    # Override the summarize_results function imported in agent.py to avoid recursion
    monkeypatch.setattr("cognita.agent.summarize_results", lambda results: {"final_summary": results.get("summary")})
    
    return agent

def test_execute_query_success(dummy_agent):
    """
    Test that a valid query returns the expected output.
    """
    valid_query = "What are the latest advancements in artificial intelligence?"
    result = dummy_agent.execute_query(valid_query)
    assert result == {"final_summary": "Test summary"}

def test_execute_query_invalid_query(dummy_agent):
    """
    Test that an invalid query (e.g., too short) triggers a ProcessingError.
    """
    invalid_query = "short"
    with pytest.raises(ProcessingError):
        dummy_agent.execute_query(invalid_query)
