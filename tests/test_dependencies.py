import pytest

def test_spacy():
    import spacy
    nlp = spacy.load("en_core_web_sm")
    assert nlp is not None

def test_torch():
    import torch
    assert torch.__version__ == "1.10.0+cpu"

def test_transformers():
    from transformers import pipeline
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    assert summarizer is not None

def test_pdf():
    import PyPDF2
    assert PyPDF2.__version__ == "3.0.1"
