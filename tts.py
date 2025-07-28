import pyttsx3
from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play

class VoiceOutput:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        
    def speak_offline(self, text, lang):
        try:
            if lang == 'ar':
                self.engine.setProperty('voice', 'mb-ar1')  # Arabic voice
            else:
                self.engine.setProperty('voice', 'english')
                
            print(f"Bot ({lang.upper()}): {text}")
            self.engine.say(text)
            self.engine.runAndWait()
        except:
            self.speak_online(text, lang)
    
    def speak_online(self, text, lang):
        try:
            print(f"Bot ({lang.upper()}): {text}")
            tts = gTTS(text=text, lang='ar' if lang == 'ar' else 'en')
            tts.save("response.mp3")
            
            # Convert to wav for better compatibility
            sound = AudioSegment.from_mp3("response.mp3")
            sound.export("response.wav", format="wav")
            os.system("aplay response.wav")  # Linux audio player
        except Exception as e:
            print(f"TTS Error: {e}")
