import PyPDF2
from transformers import pipeline
import spacy
import logging
import numpy as np

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_nlp():
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        logging.warning("Downloading spacy model...")
        spacy.cli.download("en_core_web_sm")
        return spacy.load("en_core_web_sm")

nlp = initialize_nlp()

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def chunk_text(text, chunk_size=1000):
    """Split text into chunks that transformers can process."""
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0
    
    for word in words:
        current_length += len(word) + 1  # +1 for space
        if current_length > chunk_size:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]
            current_length = len(word)
        else:
            current_chunk.append(word)
            
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    return chunks

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file with error handling."""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        if not text.strip():
            raise ValueError("No text extracted from PDF")
        return text
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {str(e)}")
        raise

def summarize_text(text, max_length=500):
    """Summarize text with chunking for long texts."""
    try:
        if len(text) > 1000:
            chunks = chunk_text(text)
            summaries = []
            for chunk in chunks:
                summary = summarizer(chunk, max_length=max_length//len(chunks), 
                                  min_length=30, do_sample=False)
                summaries.append(summary[0]['summary_text'])
            return ' '.join(summaries)
        else:
            summary = summarizer(text, max_length=max_length, min_length=30, 
                               do_sample=False)
            return summary[0]['summary_text']
    except Exception as e:
        logger.error(f"Error summarizing text: {str(e)}")
        raise

def extract_key_points(text):
    """Extract key points with improved filtering."""
    try:
        doc = nlp(text)
        sentences = list(doc.sents)
        # Filter for meaningful sentences
        key_points = [
            sent.text for sent in sentences
            if (len(sent) > 10 and  # Longer sentences
                any(token.pos_ in ['VERB', 'NOUN'] for token in sent) and  # Contains verbs/nouns
                not any(token.is_stop for token in sent[:2]))  # Doesn't start with stop words
        ]
        return key_points[:5]  # Return top 5 key points
    except Exception as e:
        logger.error(f"Error extracting key points: {str(e)}")
        raise
