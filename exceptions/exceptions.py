from fastapi import HTTPException


HTTP_EXCEPTION_SERVER_500 = HTTPException(
    status_code=500,
    detail="Ошибка из Deepali API"
)

HTTP_EXCEPTION_SERVER_400 = HTTPException(
    status_code=400,
    detail="Разрешены только изображения в форматах .jpg и .png"
)
