from openai import OpenAI
from typing import Dict, Any
from os import getenv, environ
from dotenv import load_dotenv
from src.prompts.extraction import EXTRACTION_PROMPT
from src.prompts.assistant import AI_ASSISTANT, GENERIC_AI_ASSISTANT

load_dotenv()

environ["OPENAI_API_KEY"] = getenv("OPENAI_API_KEY")
OPENAI_MODEL_NAME = getenv("OPENAI_MODEL_NAME", "gpt-5-mini")


class LLM:
    def __init__(self):
        self.openai_client = OpenAI()
        self.model_name = OPENAI_MODEL_NAME

    async def extraction_preference(self, chat_history: str) -> Dict[str, Any]:

        response = self.openai_client.responses.create(
            model=self.model_name,
            input=EXTRACTION_PROMPT.format(
                chat_history=chat_history
            )
        )

        return response.output_text
    
    async def generate_ai_assistant(self, user_query: str, user_memory: dict) ->  str:
        response = self.openai_client.responses.create(
            model=self.model_name,
            input=AI_ASSISTANT.format(
                user_query=user_query,
                user_memory=user_memory
            )
        )

        return response.output_text

    async def generate_generic_ai_assistant(self, user_query: str) -> str:
        response = self.openai_client.responses.create(
            model=self.model_name,
            input=GENERIC_AI_ASSISTANT.format(
                user_query=user_query,
            )
        )

        return response.output_text
