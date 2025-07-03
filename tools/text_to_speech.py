
#--------------------------------------------------------------------------------------

# import os
# import tempfile
# import time
# from typing import Dict
# from gtts import gTTS
# import streamlit as st
# from crewai.tools import BaseTool
# import re
# import pygame

# class TextToSpeechTool(BaseTool):
#     name: str = "Human TTS Tool"
#     description: str = "Reads aloud text sentence by sentence with live display."

#     def _run(self, text: str, speed: str = "normal") -> Dict:
#         if not text.strip():
#             return {"status": "No text to read", "duration": 0, "audio_path": ""}

#         # Sentence splitting (basic)
#         sentences = re.split(r'(?<=[.!?])\s+', text.strip())

#         # Speed control
#         slow = speed == "slow"

#         # Init duration tracker
#         total_duration = 0
#         st.subheader("📖 Reading the Document")
#         sentence_display = st.empty()

#         for sentence in sentences:
#             if not sentence.strip():
#                 continue

#             # Show sentence in UI
#             sentence_display.markdown(f"🗣️ **{sentence.strip()}**")

#             # Generate audio for sentence
#             tts = gTTS(text=sentence.strip(), lang='en', slow=slow)
#             fd, path = tempfile.mkstemp(suffix=".mp3")
#             tts.save(path)

#             # Play it
#             pygame.mixer.init()
#             pygame.mixer.music.load(path)
#             pygame.mixer.music.play()

#             # Wait until playback finishes
#             while pygame.mixer.music.get_busy():
#                 time.sleep(0.1)

#             pygame.mixer.quit()
#             os.remove(path)

#             # Simulate sentence duration (approx.)
#             total_duration += len(sentence.split()) / (100 if slow else 150)

#         return {
#             "status": "Reading completed.",
#             "duration": round(total_duration, 2),
#             "audio_path": ""  # Not returning full audio path as audio is played inline
#         }


import os
import tempfile
import time
from typing import Dict
from gtts import gTTS
import streamlit as st
from crewai.tools import BaseTool
import re
import pygame

class TextToSpeechTool(BaseTool):
    name: str = "Human TTS Tool"
    description: str = "Reads aloud text sentence by sentence with live display."

    def _run(self, text: str, speed: str = "normal") -> Dict:
        if not text.strip():
            return {"status": "No text to read", "duration": 0, "audio_path": ""}

        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        slow = speed == "slow"
        total_duration = 0
        st.subheader("📖 Reading the Document")
        sentence_display = st.empty()

        for sentence in sentences:
            if not sentence.strip():
                continue

            sentence_display.markdown(f"🗣️ **{sentence.strip()}**")

            tts = gTTS(text=sentence.strip(), lang='en', slow=slow)
            fd, path = tempfile.mkstemp(suffix=".mp3")
            tts.save(path)

            pygame.mixer.init()
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(0.1)

            pygame.mixer.quit()
            os.remove(path)

            total_duration += len(sentence.split()) / (100 if slow else 150)

        return {
            "status": "Reading completed.",
            "duration": round(total_duration, 2),
            "audio_path": ""
        }
