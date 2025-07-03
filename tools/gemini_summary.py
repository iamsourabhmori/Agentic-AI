# from crewai.tools import BaseTool
# from typing import Optional
# from vertexai.language_models import TextGenerationModel

# class GeminiSummaryTool(BaseTool):
#     name: str = "Gemini Summarizer"
#     description: str = "Summarizes text using Gemini Pro."

#     def _run(self, text: str) -> Optional[str]:
#         try:
#             model = TextGenerationModel.from_pretrained("gemini-2.0-flash")
#             response = model.predict(
#                 prompt=f"Summarize the following in 3-5 lines:\n{text}",
#                 temperature=0.5,
#                 max_output_tokens=512
#             )
#             return response.text.strip()
#         except Exception as e:
#             return f"Failed to generate summary: {e}"



# import os
# from crewai.tools import BaseTool
# from typing import Optional
# import google.generativeai as genai
# from dotenv import load_dotenv

# class GeminiSummaryTool(BaseTool):
#     name: str = "Gemini Summarizer"
#     description: str = "Summarizes text using Gemini Pro via API Key."

#     def _run(self, text: str) -> Optional[str]:
#         try:
#             # Load environment variables
#             load_dotenv()
#             api_key = os.getenv("GEMINI_API_KEY")
#             if not api_key:
#                 return "API key not found in environment."

#             # Configure Gemini API
#             genai.configure(api_key=api_key)

#             model = genai.GenerativeModel("gemini-pro")

#             prompt = f"Summarize the following text in 3-5 bullet points:\n\n{text}"

#             response = model.generate_content(prompt)
#             return response.text.strip()

#         except Exception as e:
#             return f"Failed to generate summary: {e}"

#-------------------------------------

# import os
# from crewai.tools import BaseTool
# from typing import Optional
# import google.generativeai as genai
# from dotenv import load_dotenv

# class GeminiSummaryTool(BaseTool):
#     name: str = "Gemini Summarizer"
#     description: str = "Summarizes text using Gemini Pro via API Key."

#     def _run(self, text: str) -> Optional[str]:
#         try:
#             load_dotenv()
#             api_key = os.getenv("GEMINI_API_KEY")
#             if not api_key:
#                 return "API key not found in environment."

#             genai.configure(api_key=api_key)
#             model = genai.GenerativeModel("gemini-pro")

#             prompt = f"""
# You are a helpful assistant summarizing a document for a human listener.

# Please summarize the following PDF document content like Gemini's document summarizer:
# - Focus on the main ideas and key takeaways.
# - Avoid any technical/code content or headers.
# - Use 4–6 clear, natural-sounding bullet points.

# Document content:
# {text}
# """

#             response = model.generate_content(prompt)
#             return response.text.strip()
#         except Exception as e:
#             return f"Failed to generate summary: {e}"


#---------------------------------------------------------------
# import os
# from crewai.tools import BaseTool
# from typing import Optional
# import google.generativeai as genai
# from dotenv import load_dotenv

# class GeminiSummaryTool(BaseTool):
#     name: str = "Gemini Summarizer"
#     description: str = "Summarizes text using Gemini Pro via API Key."

#     def _run(self, text: str) -> Optional[str]:
#         try:
#             load_dotenv()
#             api_key = os.getenv("GEMINI_API_KEY")
#             if not api_key:
#                 return "API key not found in environment."

#             genai.configure(api_key=api_key)

#             model = genai.GenerativeModel(model_name="gemini-pro")

#             prompt = f"""
# You are a helpful assistant summarizing a document for a human listener.

# Please summarize the following PDF document content like Gemini's document summarizer:
# - Focus on the main ideas and key takeaways.
# - Avoid any technical/code content or headers.
# - Use 4–6 clear, natural-sounding bullet points.

# Document content:
# {text}
# """

#             # ✅ use `generate_content()` with a list of parts for `gemini-pro`
#             response = model.generate_content([prompt])

#             return response.text.strip()

#         except Exception as e:
#             return f"Failed to generate summary: {e}"

#------------------------------------------------------------------------------------
import os
from crewai.tools import BaseTool
from typing import Optional
import google.generativeai as genai
from dotenv import load_dotenv

class GeminiSummaryTool(BaseTool):
    name: str = "Gemini Summarizer"
    description: str = "Summarizes text using Gemini 1.5 Pro via API Key."

    def _run(self, text: str) -> Optional[str]:
        try:
            load_dotenv()
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                return "API key not found in environment."

            genai.configure(api_key=api_key)

            # ✅ Use the latest, supported model
            model = genai.GenerativeModel(model_name="gemini-2.5-pro")

            prompt = f"""
You are a helpful assistant summarizing a document.

Summarize the following PDF content into 4-6 clear bullet points:
{text}
"""

            response = model.generate_content([prompt])
            return response.text.strip()

        except Exception as e:
            return f"Failed to generate summary: {e}"





