from loguru import logger
from src.requests import PersonaQuery
from fastapi import APIRouter, Form, HTTPException
from src.services import extract_user_memory_service, query_persona_ai_service

persona_ai_router = APIRouter(prefix="/api/v1", tags=["PersonaAI"])


@persona_ai_router.post("/user-extraction")
async def extract_user_memory(
    calm_mentor_chat: bool = Form(False, description="To use calm mentor based chat"),
    witty_friend_chat: bool = Form(False, description="To use witty friend based chat"),
    therapist_style_chat: bool = Form(False, description="To use therapist style based chat")
):
    # Check if more than one variable is True
    if [calm_mentor_chat, witty_friend_chat, therapist_style_chat].count(True) > 1:
        logger.error("Only one field can be True at a time")
        raise HTTPException(
            status_code=400,
            detail="Only field can be True at a time"
        )
    # Check if more than two variable are False
    elif [calm_mentor_chat, witty_friend_chat, therapist_style_chat].count(False) > 2:
        logger.error("Atleast one field should be True")
        raise HTTPException(
            status_code=400,
            detail="Atleast 1 field should be True"
        )

    return await extract_user_memory_service(
        calm_mentor_chat,
        witty_friend_chat,
        therapist_style_chat
    )


@persona_ai_router.post("/persona-ai-assistant")
async def query_persona_ai(payload: PersonaQuery):
    return await query_persona_ai_service(payload)