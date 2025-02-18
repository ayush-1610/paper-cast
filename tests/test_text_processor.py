import pytest
from src.text_processor import chunk_text, summarize_text, extract_key_points

def test_chunk_text():
    text = "This is a test text" * 100
    chunks = chunk_text(text, chunk_size=100)
    assert all(len(chunk) <= 100 for chunk in chunks)

def test_extract_key_points():
    text = "This is a test. This is another test. Third test sentence."
    points = extract_key_points(text)
    assert isinstance(points, list)
    assert len(points) <= 5
