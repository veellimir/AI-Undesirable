from fastapi import APIRouter

from core.settings import settings
from .router_moderation import router as r_moderation


router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(r_moderation)
