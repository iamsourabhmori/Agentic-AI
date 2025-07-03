'''

import streamlit as st
import os
import sys
import time
import speech_recognition as sr

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.pdf_to_audio_agent import run_agent
from tools.text_to_speech import TextToSpeechTool
from tools.gemini_summary import GeminiSummaryTool

st.set_page_config(page_title="📖 PDF Reader Agent", page_icon="📘")
st.title("📖 Human-like PDF Reader")

uploaded_file = st.file_uploader("📂 Upload a PDF", type=["pdf"])

def listen_for_user_input() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎧 Listening... Please ask or say anything.")
        r.adjust_for_ambient_noise(source, duration=3)
        try:
            audio = r.listen(source, timeout=10)
            user_input = r.recognize_google(audio)
            return user_input
        except sr.UnknownValueError:
            return "UNRECOGNIZED"
        except sr.WaitTimeoutError:
            return "TIMEOUT"
        except Exception as e:
            return f"ERROR: {str(e)}"

if uploaded_file:
    os.makedirs("documents", exist_ok=True)
    pdf_path = os.path.join("documents", uploaded_file.name)

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    st.info("⏳ Preparing to read the document...")
    time.sleep(3)

    result = run_agent(pdf_path)

    if "error" in result:
        st.error(result["error"])
    else:
        st.subheader("📄 Extracted Text")
        st.text_area("PDF Content", result["text"], height=300)

        # 🔊 Auto-play extracted text
        if "audio_path" in result and os.path.exists(result["audio_path"]):
            st.audio(result["audio_path"], format="audio/mp3", start_time=0)
            st.success(f"✅ Document reading done in {result['duration']} seconds.")

        # Show Gemini Summary
        st.subheader("🧠 Gemini Summary")
        st.info(result["summary"])

        # 🎤 Listen to user's voice and send it to Gemini
        user_query = listen_for_user_input()

        if user_query not in ["UNRECOGNIZED", "TIMEOUT"] and not user_query.startswith("ERROR"):
            st.warning(f"🗣️ You said: \"{user_query}\"")

            # Build context-aware prompt
            prompt = f"""The user just read a document and then said:
\"{user_query}\"

Here is the document content for context:
{result['text']}

Please respond appropriately and clearly."""
            
            gemini = GeminiSummaryTool()
            gemini_reply = gemini._run(prompt)

            st.subheader("💬 Gemini's Response")
            st.write(gemini_reply)

            # Speak the Gemini response
            st.info("🔊 Reading Gemini's response...")
            tts = TextToSpeechTool()
            reply_audio = tts._run(gemini_reply)
            if os.path.exists(reply_audio["audio_path"]):
                st.audio(reply_audio["audio_path"], format="audio/mp3")

        elif user_query == "UNRECOGNIZED":
            st.error("🛑 Could not understand your voice.")
        elif user_query == "TIMEOUT":
            st.warning("⌛ You didn’t say anything. Try again.")
        elif user_query.startswith("ERROR"):
            st.error(f"❌ Audio error: {user_query}")
'''