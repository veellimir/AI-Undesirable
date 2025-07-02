from typing import Dict, Any

import httpx

from core.settings import settings
from exceptions.exceptions import HTTP_EXCEPTION_SERVER_500


async def check_nsfw_content(image_bytes: bytes, filename: str, content_type: str) -> float:
    headers: Dict[str, str] = {
        "api-key": settings.DEEPAI_KEY
    }
    files: Dict[str, Any] = {
        "image": (filename, image_bytes, content_type)
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            settings.DEEPAI_URL, headers=headers, files=files
        )
    if response.status_code != 200:
        print("DeepAI response:", response.status_code, response.text)
        raise HTTP_EXCEPTION_SERVER_500

    result = response.json()
    nsfw_score = result.get("output", {}).get("nsfw_score", 0)
    return nsfw_score
