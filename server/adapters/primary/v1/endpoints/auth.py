from fastapi import APIRouter
from server.core.injectable import injectable

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post("/sign-in")
@injectable
def sign_in():
    return {
        "statusCode": 200,
        "message": "Sign in successfully",
        "payload": {
            "accessToken": "accessToken",
            "refreshToken": "refreshToken"
        }
    }