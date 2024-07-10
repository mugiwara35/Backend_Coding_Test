from typing import Dict, Any
from fastapi import HTTPException, status
import random
import string

# Fungsi utilitas untuk membuat respon sukses
def success_response(data: Dict[str, Any], message: str = "success", status_code: int = status.HTTP_200_OK) -> Dict[str, Any]:
    return {
        "status": "success",
        "message": message,
        "data": data, 
        "status_code": status_code
    }
    
# Fungsi utilitas untuk membuat respon error
def error_response(message: str, reason: str = "None", status_code: int = status.HTTP_400_BAD_REQUEST) -> HTTPException:
    error_body = {
        "status": "error",
        "message": message,
        "reason": reason,
    }
    return HTTPException(status_code=status_code, detail=error_body)

def generate_random_code(length=6):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))