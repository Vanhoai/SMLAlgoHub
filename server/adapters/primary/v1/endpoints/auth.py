from fastapi import APIRouter, Request

from server.core.injectable import injectable

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post("/sign-in")
async def sign_in(req: Request):

    client_host = req.client.host
    print("client_host", client_host)

    return {
        "statusCode": 200,
        "message": "Sign in successfully",
        "payload": {
            "accessToken": "accessToken",
            "refreshToken": "refreshToken"
        }
    }