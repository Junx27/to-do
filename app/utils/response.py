from fastapi.responses import JSONResponse
from typing import Any

def success_response(data: Any = None, message: str = "OK", status_code: int = 200):
    return JSONResponse(
        status_code=status_code,
        content={
            "status": status_code,
            "message": message,
            "data": data,
        }
    )

def not_found_response():
    return JSONResponse(
        status_code=404,
        content={
            "status": "Failed",
            "message": "Not found"
        }
    )