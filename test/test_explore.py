"""Unit tests for Countdown Letters"""
import pytest
import countdown_oracle.src.explore as ex

def test_apple():
    """Try the letters for apple backwards"""
    words = ex.permut_words("elppa")
    assert "apple" in words
