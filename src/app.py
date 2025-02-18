import sys
import os
import logging
from flask import Flask, render_template, request, send_file, flash, session
from werkzeug.security import safe_join
import secrets

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add src directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.paper_fetcher import fetch_paper
from src.text_processor import extract_text_from_pdf, summarize_text, extract_key_points
from src.conversation_generator import generate_conversation
from src.tts_engine import text_to_speech

app = Flask(__name__,
           template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'),
           static_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static'))

# Replace the existing secret key generation
app.secret_key = secrets.token_hex(32)

# Add CSRF protection
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        if not query:
            flash('Please enter a search query', 'error')
            return render_template('index.html')
            
        try:
            logger.info(f"Processing query: {query}")
            
            # Fetch paper
            pdf_path = fetch_paper(query)
            if not pdf_path:
                flash('No papers found for the given query', 'error')
                return render_template('index.html')
            
            # Store the path in session
            session['pdf_path'] = pdf_path
            
            # Process text
            text = extract_text_from_pdf(pdf_path)
            summary = summarize_text(text)
            key_points = extract_key_points(text)
            
            # Generate conversation
            script = generate_conversation(summary, key_points)
            
            # Convert to audio
            audio_path = text_to_speech(script)
            
            # Store generated content in session
            session['audio_path'] = audio_path
            
            return render_template('podcast.html', 
                                 audio_path=os.path.relpath(audio_path, app.static_folder))
                                 
        except Exception as e:
            logger.error(f"Error processing request: {str(e)}")
            flash(f'Error: {str(e)}', 'error')
            return render_template('index.html')
    
    return render_template('index.html')

if __name__ == "__main__":
    # Create necessary directories
    os.makedirs(os.path.join(app.static_folder, 'audio'), exist_ok=True)
    os.makedirs(os.path.join(os.path.dirname(app.root_path), 'data'), exist_ok=True)
    
    app.run(debug=True)
