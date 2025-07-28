Here's a comprehensive `README.md` file for your bilingual chatbot project:

# Bilingual Chatbot (English & Arabic) 🗣️🌍

A voice-enabled chatbot that understands and responds in both English and Arabic, using offline speech recognition and text generation.

## Features ✨
- **Speech-to-Text**: Voice input in English/Arabic using VOSK
- **AI Responses**: GPT-style text generation with Transformers
- **Text-to-Speech**: Voice output in both languages
- **Language Switching**: Voice command to change languages
- **Offline Capable**: Works without internet (except for optional online TTS fallback)

## System Requirements 💻
- **OS**: Linux Mint (or any Ubuntu/Debian-based distro)
- **RAM**: Minimum 4GB (8GB recommended for better performance)
- **Storage**: 5GB free space (for models and dependencies)
- **Python**: 3.8 or higher

## Installation ⚙️

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/bilingual-chatbot.git
cd bilingual-chatbot
```

### 2. Install system dependencies
```bash
sudo apt update && sudo apt install -y \
    python3-pip python3-venv \
    portaudio19-dev libportaudio2 \
    espeak ffmpeg mpg123 mbrola-ar1 \
    alsa-utils pulseaudio
```

### 3. Set up Python environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Download AI Models
```bash
# English model (50MB)
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip

# Arabic model (1.1GB)
wget https://storage.googleapis.com/vosk-models/vosk-model-ar-mgb2-0.4.zip
unzip vosk-model-ar-mgb2-0.4.zip
```

⚠️ **Note**: The full AI model files are not included in this repository due to their large size (total >1.5GB). You must download them separately using the commands above.

## Usage 🚀
```bash
source venv/bin/activate
python main.py
```

**Voice Commands**:
- "switch language" - Toggle between English/Arabic
- "exit" - Quit the application

## Project Structure 📂
```
bilingual-chatbot/
├── vosk-model-small-en-us-0.15/  # English STT model (download separately)
├── vosk-model-ar-mgb2-0.4/      # Arabic STT model (download separately)
├── stt.py                       # Speech-to-text processing
├── llm.py                       # AI response generation
├── tts.py                       # Text-to-speech output
├── main.py                      # Main application
├── requirements.txt             # Python dependencies
└── README.md
```

## Troubleshooting 🔧
### Audio Issues
```bash
# Check microphone
arecord -l

# Test audio input
arecord -d 5 test.wav && aplay test.wav
```

### Python Errors
```bash
# Recreate virtual environment if needed
rm -rf venv/
python3 -m venv venv
source venv/bin/activate
pip install --force-reinstall -r requirements.txt
```

## Limitations ⚠️
1. Arabic support is Modern Standard Arabic (may not handle all dialects perfectly)
2. Larger AI models not included - must be downloaded separately
3. Performance depends on your CPU (no GPU acceleration in this version)

## License 📄
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note for Collaborators**: The VOSK model files (`vosk-model-*`) are intentionally excluded from version control via `.gitignore` due to their large size. All users must download them separately using the provided commands.
