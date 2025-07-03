

#---------------------------------------------------------------------------------------------------------
# '''
# import streamlit as st
# import os
# import sys
# import time
# import speech_recognition as sr

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from agents.pdf_to_audio_agent import run_agent
# from tools.text_to_speech import TextToSpeechTool
# from tools.gemini_summary import GeminiSummaryTool

# st.set_page_config(page_title="📖 PDF Reader Agent", page_icon="📘")
# st.title("📖 Human-like PDF Reader")

# uploaded_file = st.file_uploader("📂 Upload a PDF", type=["pdf"])

# def listen_for_understanding() -> str:
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.info("🎧 Listening for 'I don't understand'...")
#         r.adjust_for_ambient_noise(source, duration=10)
#         try:
#             audio = r.listen(source, timeout=10)
#             user_input = r.recognize_google(audio)
#             return user_input
#         except sr.UnknownValueError:
#             return "UNRECOGNIZED"
#         except sr.WaitTimeoutError:
#             return "TIMEOUT"
#         except Exception as e:
#             return f"ERROR: {str(e)}"

# if uploaded_file:
#     os.makedirs("documents", exist_ok=True)
#     pdf_path = os.path.join("documents", uploaded_file.name)

#     with open(pdf_path, "wb") as f:
#         f.write(uploaded_file.read())

#     st.info("⏳ Preparing to read the document...")
#     time.sleep(3)

#     result = run_agent(pdf_path)

#     if "error" in result:
#         st.error(result["error"])
#     else:
#         st.subheader("📄 Extracted Text")
#         st.text_area("PDF Content", result["text"], height=300)

#         # 🔊 Auto-play extracted text
#         if "audio_path" in result and os.path.exists(result["audio_path"]):
#             st.audio(result["audio_path"], format="audio/mp3", start_time=0)
#             st.success(f"✅ Document reading done in {result['duration']} seconds.")

#         # Show Gemini Summary
#         st.subheader("🧠 Gemini Summary")
#         st.info(result["summary"])

#         # 🎤 Automatically listen for "I don't understand"
#         user_feedback = listen_for_understanding()

#         if "don't understand" in user_feedback.lower():
#             st.warning("Detected: User doesn't understand. Simplifying...")
#             explainer = GeminiSummaryTool()
#             simple_summary = explainer._run("Explain in simplest way:\n" + result["text"])

#             st.subheader("📚 Simplified Summary")
#             st.write(simple_summary)

#             st.info("🔊 Reading simplified summary...")
#             tts = TextToSpeechTool()
#             summary_audio = tts._run(simple_summary)
#             if os.path.exists(summary_audio["audio_path"]):
#                 st.audio(summary_audio["audio_path"], format="audio/mp3")

#         elif user_feedback == "UNRECOGNIZED":
#             st.error("🛑 Could not understand your voice.")
#         elif user_feedback == "TIMEOUT":
#             st.warning("⌛ You didn’t say anything. Try again by re-uploading.")
#         elif user_feedback.startswith("ERROR"):
#             st.error(f"❌ Audio error: {user_feedback}")
# '''
# #------------------------------------------------------------------------

# import streamlit as st
# import os
# import sys
# import time
# import re
# import speech_recognition as sr

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from agents.pdf_to_audio_agent import run_agent
# from tools.text_to_speech import TextToSpeechTool
# from tools.gemini_summary import GeminiSummaryTool

# st.set_page_config(page_title="📖 PDF Reader Agent", page_icon="📘")
# st.title("📖 Human-like PDF Reader")

# uploaded_file = st.file_uploader("📂 Upload a PDF", type=["pdf"])

# def listen_for_user_input() -> str:
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.info("🎧 Listening... Please ask or say anything.")
#         r.adjust_for_ambient_noise(source, duration=3)
#         try:
#             audio = r.listen(source, timeout=10)
#             user_input = r.recognize_google(audio)
#             return user_input
#         except sr.UnknownValueError:
#             return "UNRECOGNIZED"
#         except sr.WaitTimeoutError:
#             return "TIMEOUT"
#         except Exception as e:
#             return f"ERROR: {str(e)}"

# def strip_code_blocks(text):
#     # Remove triple-backtick blocks and any likely code patterns
#     text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
#     text = re.sub(r"\b(import|def|class|from|return)\b.*", "", text)
#     return text.strip()

# if uploaded_file:
#     os.makedirs("documents", exist_ok=True)
#     pdf_path = os.path.join("documents", uploaded_file.name)

#     with open(pdf_path, "wb") as f:
#         f.write(uploaded_file.read())

#     st.info("⏳ Preparing to read the document...")
#     time.sleep(3)

#     result = run_agent(pdf_path)

#     if "error" in result:
#         st.error(result["error"])
#     else:
#         st.subheader("📄 Extracted Text")
#         st.text_area("PDF Content", result["text"], height=300)

#         # 🔊 Auto-play extracted text
#         if "audio_path" in result and os.path.exists(result["audio_path"]):
#             st.audio(result["audio_path"], format="audio/mp3", start_time=0)
#             st.success(f"✅ Document reading done in {result['duration']} seconds.")

#         # Show Gemini Summary
#         st.subheader("🧠 Gemini Summary")
#         clean_summary = strip_code_blocks(result["summary"])
#         st.info(clean_summary)

#         # 🎤 Listen to user's voice and send it to Gemini
#         user_query = listen_for_user_input()

#         if user_query not in ["UNRECOGNIZED", "TIMEOUT"] and not user_query.startswith("ERROR"):
#             st.warning(f"🗣️ You said something. Processing your request...")

#             # Build clean, instruction-safe prompt
#             prompt = f"""
# The user read a document and asked: "{user_query}"

# Based on the content below, respond in plain language (no code, no syntax):

# --- DOCUMENT START ---
# {result['text']}
# --- DOCUMENT END ---
# """
#             gemini = GeminiSummaryTool()
#             gemini_reply = gemini._run(prompt)
#             clean_reply = strip_code_blocks(gemini_reply)

#             st.subheader("💬 Gemini's Response")
#             st.write(clean_reply)

#             st.info("🔊 Reading Gemini's response...")
#             tts = TextToSpeechTool()
#             reply_audio = tts._run(clean_reply)
#             if os.path.exists(reply_audio["audio_path"]):
#                 st.audio(reply_audio["audio_path"], format="audio/mp3")

#         elif user_query == "UNRECOGNIZED":
#             st.error("🛑 Could not understand your voice.")
#         elif user_query == "TIMEOUT":
#             st.warning("⌛ You didn’t say anything. Try again.")
#         elif user_query.startswith("ERROR"):
#             st.error(f"❌ Audio error: {user_query}")


#------------------------------------------------------------
import streamlit as st
import os
import sys
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.pdf_to_audio_agent import run_agent
from tools.text_to_speech import TextToSpeechTool

st.set_page_config(page_title="📖 PDF Reader Agent", page_icon="📘")
st.title("📖 Human-like PDF Reader")

uploaded_file = st.file_uploader("📂 Upload a PDF", type=["pdf"])

def strip_code_blocks(text):
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"\b(import|def|class|from|return)\b.*", "", text)
    return text.strip()

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

        st.success(f"✅ Document reading done in {result['duration']} seconds.")

        # Show Gemini Summary
        st.subheader("🧠 Gemini Summary")
        clean_summary = strip_code_blocks(result["summary"])
        st.info(clean_summary)

        # Speak the summary immediately
        st.subheader("🔊 Speaking the Summary")
        tts = TextToSpeechTool()
        summary_audio = tts._run(clean_summary)
        if os.path.exists(summary_audio["audio_path"]):
            st.audio(summary_audio["audio_path"], format="audio/mp3")
