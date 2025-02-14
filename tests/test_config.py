import pytest
from cognita.config import Config

def test_config_load(monkeypatch):
    """
    Test that configuration loads correctly from environment variables.
    """
    monkeypatch.setenv("API_BASE_URL", "http://testapi.com")
    monkeypatch.setenv("API_KEY", "testkey")
    monkeypatch.setenv("API_TIMEOUT", "15")
    monkeypatch.setenv("MAX_RESULTS", "7")
    monkeypatch.setenv("MIN_CONFIDENCE", "0.85")
    
    config = Config()
    assert config.API_BASE_URL == "http://testapi.com"
    assert config.API_KEY == "testkey"
    assert config.API_TIMEOUT == 15
    assert config.MAX_RESULTS == 7
    assert config.MIN_CONFIDENCE == pytest.approx(0.85)

def test_config_missing_api_key(monkeypatch):
    """
    Test that configuration raises a ValueError when API_KEY is not set.
    """
    # Ensure API_KEY is not in the environment
    monkeypatch.delenv("API_KEY", raising=False)
    with pytest.raises(ValueError):
        Config()
