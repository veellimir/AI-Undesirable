from fastapi import APIRouter, UploadFile, File

from core.settings import settings
from exceptions.exceptions import HTTP_EXCEPTION_SERVER_400
from services.api_deep import check_nsfw_content

router = APIRouter(
    prefix=settings.api.v1.moderation,
    tags=["Модерация"]
)


# 🌐🔁 ──────────────── ROUTERS MODERATION ──────────────── 🔁🌐

@router.post("/moderate")
async def moderate_image(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTP_EXCEPTION_SERVER_400

    image_bytes = await file.read()
    nsfw_score = await check_nsfw_content(
        image_bytes=image_bytes,
        filename=file.filename,
        content_type=file.content_type,
    )
    if nsfw_score > 0.7:
        return {"status": "REJECTED", "reason": "NSFW content"}
    return {"status": "OK"}
