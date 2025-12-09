from loguru import logger
from src.utils.llm import LLM
from fastapi import HTTPException
from src.utils.json_parser import json_parser
from chat_histories import before_calm_mentor_chat, before_therapist_style_chat, before_witty_friend_chat


async def extract_user_memory_service(
        calm_mentor_chat,
        witty_friend_chat,
        therapist_style_chat
):
    try:

        if calm_mentor_chat:
            history = before_calm_mentor_chat.CHAT
        elif witty_friend_chat:
            history = before_witty_friend_chat.CHAT
        elif therapist_style_chat:
            history = before_therapist_style_chat.CHAT

        llm = LLM()

        llm_response = await llm.extraction_preference(chat_history=history)
        json_response = await json_parser(llm_response)

        return json_response

    except Exception as e:
        logger.error(f"User Memory Extraction Error: {e}")
        raise HTTPException(
            status_code=400,
            detail=f"User Memory Extraction Error: {e}"
        )


async def query_persona_ai_service(payload):
    try:
        llm = LLM()

        llm_response = await llm.generate_ai_assistant(
            user_query=payload.query,
            user_memory=payload.user_memory
        )

        return llm_response

    except Exception as e:
        logger.error(f"Quering Persona AI Error: {e}")
        raise HTTPException(
            status_code=400,
            detail=f"Quering Persona AI Error: {e}"
        )
