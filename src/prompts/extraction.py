EXTRACTION_PROMPT = """You are an AI assistant tasked with analyzing a conversation between a user and an assistant. Your goal is to extract meaningful insights about the user, including their preferences, emotional patterns, and factual information that may be worth remembering. 

**Chat History**: {chat_history}

Instructions:
1. Read the full chat history provided below.
2. Identify the user's **preferences** (topics they like, communication style they prefer, hobbies, tones they respond well to, etc.).
3. Identify **emotional patterns** (frequent emotional states, triggers for certain emotions, tendencies like stress, frustration, happiness, humor, etc.).
4. Identify **facts worth remembering** (specific events, accomplishments, recurring activities, deadlines, personal details, etc.).
5. Return the results strictly in the following JSON format.

JSON Schema:
{{
  "preferences": {{
    "topics": [ "list of topics the user likes" ],
    "communication_style": "short description of preferred interaction style",
    "hobbies": [ "list of hobbies or interests mentioned" ],
    "tone_response": "types of tones the user responds well to, e.g., humor, calm, informative"
  }},
  "emotional_patterns": {{
    "frequent_emotions": [ "list of emotions commonly displayed" ],
    "triggers": [ "list of triggers that affect user's emotions" ],
    "behavior_tendencies": [ "how the user usually reacts emotionally" ]
  }},
  "facts": {{
    "personal_facts": [ "important personal details to remember" ],
    "recent_accomplishments": [ "list of recent achievements or milestones" ],
    "tasks_or_responsibilities": [ "key responsibilities, deadlines, or obligations" ]
  }}
}}

Return **only JSON**. Do not include explanations or extra text.
"""