import json
import numpy as np
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from langdetect import detect

class SpeechRecognizer:
    def __init__(self):
        """Initialize with English and Arabic models using sounddevice"""
        # Load VOSK models
        self.en_model = Model("vosk-model-small-en-us-0.15")
        self.ar_model = Model("vosk-model-ar-mgb2-0.4")
        self.current_model = self.en_model
        self.rec = KaldiRecognizer(self.current_model, 16000)
        
        # Sounddevice audio config
        self.sample_rate = 16000
        self.blocksize = 8192  # Buffer size
        
        # List available devices and select default mic
        print("Available audio devices:")
        print(sd.query_devices())
        self.stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            dtype='int16',
            blocksize=self.blocksize,
            device=sd.default.device[0]  # CORRECTED: Changed "device" to "device"
        )
        self.stream.start()

    def detect_language(self, text):
        """Detect if text is Arabic or English"""
        try:
            return detect(text)
        except:
            return 'en'  # Default fallback

    def listen(self):
        """Capture audio and return (text, language)"""
        print("\nListening... (Say 'switch language' to change)")
        while True:
            # Read audio buffer
            audio_data, overflowed = self.stream.read(self.blocksize)
            if overflowed:
                print("Audio buffer overflowed!")
            
            # Convert to bytes and process with VOSK
            if self.rec.AcceptWaveform(audio_data.tobytes()):
                result = json.loads(self.rec.Result())
                text = result.get('text', '').strip()
                
                if text:
                    # Language switching command
                    if "switch language" in text.lower():
                        if self.current_model == self.en_model:
                            self.current_model = self.ar_model
                            print("Switched to Arabic")
                        else:
                            self.current_model = self.en_model
                            print("Switched to English")
                        self.rec = KaldiRecognizer(self.current_model, 16000)
                        continue
                    
                    # Detect language
                    lang = self.detect_language(text)
                    return text, lang

    def __del__(self):
        """Clean up audio stream"""
        if hasattr(self, 'stream'):
            self.stream.stop()
            self.stream.close()
