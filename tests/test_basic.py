"""
Basic tests for ai-safety-guardrails
"""

import pytest

def test_basic():
    """Basic test to verify setup"""
    assert True

def test_imports():
    """Test that main module can be imported"""
    try:
        import main
        assert True
    except ImportError:
        pytest.fail("Could not import main module")
