# import os
# from crewai.tools import BaseTool
# from typing import Optional
# import openai
# from dotenv import load_dotenv

# class OpenAISummaryTool(BaseTool):
#     name: str = "OpenAI Summarizer"
#     description: str = "Summarizes text using OpenAI GPT-4."

#     def _run(self, text: str) -> Optional[str]:
#         try:
#             load_dotenv()
#             api_key = os.getenv("OPENAI_API_KEY")
#             if not api_key:
#                 return "OpenAI API key not found."

#             openai.api_key = api_key

#             response = openai.ChatCompletion.create(
#                 model="gpt-4",
#                 messages=[
#                     {"role": "system", "content": "You summarize documents in clear bullet points."},
#                     {"role": "user", "content": f"Please summarize:\n\n{text}"}
#                 ],
#                 temperature=0.3
#             )
#             return response.choices[0].message.content.strip()
#         except Exception as e:
#             return f"Failed to generate summary: {e}"




# import os
# from crewai.tools import BaseTool
# from typing import Optional
# from openai import OpenAI
# from dotenv import load_dotenv

# class OpenAISummaryTool(BaseTool):
#     name: str = "OpenAI Summarizer"
#     description: str = "Summarizes text using OpenAI GPT-4 (v1+ SDK)."

#     def _run(self, text: str) -> Optional[str]:
#         try:
#             load_dotenv()
#             api_key = os.getenv("OPENAI_API_KEY")
#             if not api_key:
#                 return "OpenAI API key not found."

#             client = OpenAI(api_key=api_key)

#             response = client.chat.completions.create(
#                 model="gpt-4",
#                 messages=[
#                     {"role": "system", "content": "You summarize documents in clear bullet points."},
#                     {"role": "user", "content": f"Please summarize the following document:\n\n{text}"}
#                 ],
#                 temperature=0.3
#             )

#             return response.choices[0].message.content.strip()
#         except Exception as e:
#             return f"Failed to generate summary: {e}"


# import os
# from crewai.tools import BaseTool
# from typing import Optional
# import google.generativeai as genai
# from dotenv import load_dotenv

# class GeminiSummaryTool(BaseTool):
#     name: str = "Gemini Summarizer"
#     description: str = "Summarizes text using Gemini 1.5 Pro via API Key."

#     def _run(self, text: str) -> Optional[str]:
#         try:
#             load_dotenv()
#             api_key = os.getenv("GEMINI_API_KEY")
#             if not api_key:
#                 return "API key not found in environment."

#             genai.configure(api_key=api_key)

#             # ✅ Use the latest, supported model
#             model = genai.GenerativeModel(model_name="gemini-1.5-pro")

#             prompt = f"""
# You are a helpful assistant summarizing a document.

# Summarize the following PDF content into 4-6 clear bullet points:
# {text}
# """

#             response = model.generate_content([prompt])
#             return response.text.strip()

#         except Exception as e:
#             return f"Failed to generate summary: {e}"
