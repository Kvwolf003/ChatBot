from stt import SpeechRecognizer
from llm import LanguageProcessor
from tts import VoiceOutput
import time

def main():
    recognizer = SpeechRecognizer()
    processor = LanguageProcessor()
    voice = VoiceOutput()
    
    print("""
    Bilingual Chatbot Activated
    ==========================
    Commands:
    - Say 'switch language' to change between English/Arabic
    - Say 'exit' to quit
    """)
    
    while True:
        try:
            # Listen for input
            text, lang = recognizer.listen()
            
            if "exit" in text.lower():
                voice.speak_offline("Goodbye!", 'en')
                break
            
            # Process and respond
            response = processor.generate_response(text, lang)
            voice.speak_offline(response, lang)
            
        except KeyboardInterrupt:
            voice.speak_offline("Session ended", 'en')
            break
        except Exception as e:
            print(f"System Error: {e}")
            time.sleep(1)  # Prevent rapid error looping

if __name__ == "__main__":
    main()
