import groq
import json
import os
import tiktoken

class LLMIntegration:
    def __init__(self, api_key=None):
        if api_key is None:
            api_key = os.environ.get("GROQ_API_KEY")
        if api_key is None:
            raise ValueError("GROQ API key not provided and not found in environment variables")
        self.client = groq.Groq(api_key=api_key)

    def _truncate_text(self, text: str, max_tokens: int = 8000) -> str:
        encoding = tiktoken.get_encoding("cl100k_base")
        encoded = encoding.encode(text)
        truncated = encoded[:max_tokens]
        return encoding.decode(truncated)

    def analyze_document(self, document_text):
        document_text = self._truncate_text(document_text)

        prompt = f"""
        Analyze the following legal document in Marathi. Provide a comprehensive analysis including a summary, key points, legal implications, and recommended actions. If you're not confident about certain aspects, please indicate that.

        Document text:
        {document_text}

        Please provide the analysis in the following JSON structure:
        {{
            "summary": "A brief summary of the entire document in English",
            "key_points": ["List of key points from the document in English"],
            "legal_implications": ["List of potential legal implications based on the document content"],
            "recommended_actions": ["List of recommended actions based on the document content"]
        }}

        Ensure that your response is valid JSON. Escape any special characters in the text fields.
        """

        response = self.client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {"role": "system", "content": "You are an AI legal assistant specialized in analyzing Marathi legal documents and providing insights in English."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=4000,
        )

        try:
            response_content = response.choices[0].message.content
            # Remove triple backticks if present
            response_content = response_content.strip('`')
            parsed_response = json.loads(response_content)
            return parsed_response
        except json.JSONDecodeError as e:
            print(f"Error parsing response: {e}")
            print("Raw response content:")
            print(response_content)
            # Try to extract JSON from the response if it's wrapped in backticks
            try:
                json_start = response_content.index('{')
                json_end = response_content.rindex('}') + 1
                json_content = response_content[json_start:json_end]
                return json.loads(json_content)
            except:
                return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None