from gtts import gTTS
import os

def text_to_speech(script, output_filename="output.mp3"):
    """
    Convert script to speech with proper path handling and error checking.
    """
    if not script:
        raise ValueError("Empty script provided for text-to-speech conversion")
        
    # Create audio directory if it doesn't exist
    audio_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                            "static", "audio")
    os.makedirs(audio_dir, exist_ok=True)
    
    output_path = os.path.join(audio_dir, output_filename)
    
    try:
        full_text = " ".join(str(line) for line in script)
        tts = gTTS(text=full_text, lang='en', slow=False)
        tts.save(output_path)
        return output_path
    except Exception as e:
        raise Exception(f"Text-to-speech conversion failed: {str(e)}")
