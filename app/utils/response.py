from fastapi.responses import JSONResponse
from typing import Any

def custom_response(data: Any = None, message: str = "OK", status_code: int = 200):
    return JSONResponse(
        status_code=status_code,
        content={
            "status": status_code,
            "message": message,
            "data": data,
        }
    )
