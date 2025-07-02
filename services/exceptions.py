from fastapi import HTTPException


HTTP_EXCEPTION_SERVER_500 = HTTPException(
    status_code=500,
    detail="Ошибка из Deepali API"
)
