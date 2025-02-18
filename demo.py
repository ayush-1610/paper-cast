import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.paper_fetcher import fetch_paper
from src.text_processor import extract_text_from_pdf, summarize_text, extract_key_points
from src.conversation_generator import generate_conversation
from src.tts_engine import text_to_speech

def run_demo():
    query = "machine learning"
    pdf_path = fetch_paper(query)
    if pdf_path:
        text = extract_text_from_pdf(pdf_path)
        summary = summarize_text(text)
        key_points = extract_key_points(text)
        script = generate_conversation(summary, key_points)
        audio_path = text_to_speech(script)
        print(f"Podcast generated at: {audio_path}")
    else:
        print("Failed to fetch paper.")

if __name__ == "__main__":
    run_demo()