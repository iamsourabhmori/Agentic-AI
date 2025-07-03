# import os
# from crewai.tools import BaseTool
# from typing import Optional
# from PyPDF2 import PdfReader

# class DocumentParserTool(BaseTool):
#     name: str = "Document Parser Tool"
#     description: str = "Extracts plain text from PDF documents."

#     def _run(self, file_path: str) -> Optional[str]:
#         if not os.path.exists(file_path):
#             return "File not found."

#         try:
#             reader = PdfReader(file_path)
#             text = ""
#             for page in reader.pages:
#                 text += page.extract_text() or ""
#             return text.strip() if text.strip() else "No readable text found in the PDF."
#         except Exception as e:
#             return f"Failed to read PDF: {e}"

#--------------------------------------------------------------

import os
from crewai.tools import BaseTool
from typing import Optional
from PyPDF2 import PdfReader

class DocumentParserTool(BaseTool):
    name: str = "Document Parser Tool"
    description: str = "Extracts plain text from PDF documents."

    def _run(self, file_path: str) -> Optional[str]:
        if not os.path.exists(file_path):
            return "File not found."

        try:
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            return text.strip() if text.strip() else "No readable text found in the PDF."
        except Exception as e:
            return f"Failed to read PDF: {e}"
