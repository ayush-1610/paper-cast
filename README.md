# PaperCAST

PaperPod is a web tool that converts research papers into engaging, conversational podcasts using AI. It fetches papers from arXiv, summarizes them, generates a script between two hosts, and converts it into audio.

## Features
- Fetch research papers from arXiv.
- Summarize and extract key points using NLP.
- Generate a conversational podcast script.
- Convert text to speech with gTTS.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PaperPod.git
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the `en_core_web_sm` model for `spacy`:
   ```bash
   python -m spacy download en_core_web_sm
   ```