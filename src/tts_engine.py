from gtts import gTTS
import os
import logging

logger = logging.getLogger(__name__)

def text_to_speech(script_lines):
    """Convert script lines to audio file."""
    try:
        audio_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'audio')
        os.makedirs(audio_dir, exist_ok=True)
        
        output_path = os.path.join(audio_dir, 'podcast.mp3')
        
        # Combine lines with pauses
        full_text = '\n'.join(script_lines)
        
        # Generate audio
        tts = gTTS(text=full_text, lang='en', slow=False)
        tts.save(output_path)
        
        return output_path
    except Exception as e:
        logger.error(f"Error in text to speech conversion: {str(e)}")
        raise
