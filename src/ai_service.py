import os
from google import genai
from google.genai import types

class GeminiSummarizer:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY não foi configurada nas variáveis de ambiente.")
        self.client = genai.Client(api_key=api_key)

    def summarize(self, text: str, max_length: str = "curto") -> str:
        prompt = f"""
        Você é um assistente especialista em síntese de textos.
        Resuma o seguinte conteúdo no formato de pontos principais ({max_length}):

        ---
        {text}
        ---
        """
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.3
            )
        )
        return response.text
