import json
from loguru import logger


async def json_parser(text: str):
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        logger.error(f"JSON parsing error:- {e}")
        return None
