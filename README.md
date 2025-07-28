# chatbot

A Python-based voice assistant that understands and responds in both English and Arabic, using offline speech recognition and text-to-speech.

## Features

- 🎙️ **Speech Recognition**: Converts speech to text using VOSK (offline)
- 🌐 **Bilingual Support**: Handles both English and Arabic
- 🔄 **Auto Language Detection**: Switches between languages automatically
- 🔊 **Text-to-Speech**: Offline (pyttsx3) and online (gTTS) fallback
- 💡 **LLM Processing**: Uses GPT-2 (English) and AraGPT-2 (Arabic)

## Installation

### Prerequisites
- Linux Mint (or any Ubuntu-based distro)
- Python 3.8+
- Microphone

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/bilingual-chatbot.git
cd bilingual-chatbot
```

### 2. Install dependencies
```bash
# System packages
sudo apt update && sudo apt install -y \
    python3-pip python3-dev python3-venv \
    portaudio19-dev libportaudio2 libportaudiocpp0 \
    espeak ffmpeg mpg123 mbrola-ar1 alsa-utils

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Python packages
pip install -r requirements.txt
```

### 3. Download language models
```bash
# English model (50MB)
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip

# Arabic model (1.1GB)
wget https://storage.googleapis.com/vosk-models/vosk-model-ar-mgb2-0.4.zip
unzip vosk-model-ar-mgb2-0.4.zip
```

## Usage

```bash
# Activate virtual environment
source venv/bin/activate

# Run the chatbot
python main.py
```

**Voice Commands:**
- "switch language" - Toggle between English/Arabic
- "exit" - Quit the program

## Project Structure

```
bilingual-chatbot/
├── vosk-model-small-en-us-0.15/    # English recognition model
├── vosk-model-ar-mgb2-0.4/         # Arabic recognition model
├── stt.py                          # Speech-to-text processing
├── llm.py                          # Language model handling
├── tts.py                          # Text-to-speech system
├── main.py                         # Main application
├── requirements.txt                # Python dependencies
└── README.md
```

## Troubleshooting

### Audio Issues
```bash
# Check microphone
arecord -l

# Test audio playback
speaker-test -t wav -c 2
```

### Common Errors
1. **"Could not import pyaudio"**:
   ```bash
   sudo apt install python3-pyaudio
   ```

2. **Arabic TTS sounds robotic**:
   ```bash
   sudo apt install --reinstall mbrola-ar1
   ```

3. **Model loading fails**:
   - Verify model paths in `stt.py`
   - Check folder permissions: `chmod -R 755 vosk-model-*`

## Customization

- **Change models**: Replace files in model directories
- **Add languages**: Download additional VOSK models
- **Modify LLM**: Edit `llm.py` to use different models

## License
MIT License - Free for personal and commercial use
```

### Key Sections Explained:

1. **Features**: Highlights the chatbot's capabilities
2. **Installation**: Step-by-step setup instructions
3. **Usage**: How to run the program
4. **Troubleshooting**: Common issues and solutions
5. **Project Structure**: File organization overview
