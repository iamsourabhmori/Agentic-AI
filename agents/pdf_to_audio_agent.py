
# from tools.document_parser import DocumentParserTool
# from tools.text_to_speech import TextToSpeechTool
# from tools.gemini_summary import GeminiSummaryTool

# def run_agent(file_path: str, speed: str = "normal") -> dict:
#     parser = DocumentParserTool()
#     tts = TextToSpeechTool()
#     summarizer = GeminiSummaryTool()

#     text = parser._run(file_path)

#     if not text or text.startswith("No readable text"):
#         return {"error": "No readable text found in PDF."}

#     tts_result = tts._run(text, speed=speed)
#     summary = summarizer._run(text)

#     return {
#         "text": text,
#         "audio_path": tts_result["audio_path"],
#         "duration": tts_result["duration"],
#         "status": tts_result["status"],
#         "summary": summary
#     }

from tools.document_parser import DocumentParserTool
from tools.text_to_speech import TextToSpeechTool
from tools.gemini_summary import GeminiSummaryTool
# from tools.openai_summary import OpenAISummaryTool 

def run_agent(file_path: str, speed: str = "normal") -> dict:
    parser = DocumentParserTool()
    tts = TextToSpeechTool()
    summarizer = GeminiSummaryTool()
    # summarizer = OpenAISummaryTool()
    text = parser._run(file_path)

    if not text or text.startswith("No readable text"):
        return {"error": "No readable text found in PDF."}

    tts_result = tts._run(text, speed=speed)
    summary = summarizer._run(text)

    return {
        "text": text,
        "audio_path": tts_result["audio_path"],
        "duration": tts_result["duration"],
        "status": tts_result["status"],
        "summary": summary
    }
