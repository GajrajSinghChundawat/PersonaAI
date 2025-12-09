from pydantic import BaseModel, Field

class UserMemory(BaseModel):
    preferences: dict
    emotional_patterns: dict
    facts: dict

class PersonaQuery(BaseModel):
    query: str = Field(..., description="Query to ask Persona AI.")
    user_memory: UserMemory = Field(..., description="User Memory extracted from `user-extraction` API")
