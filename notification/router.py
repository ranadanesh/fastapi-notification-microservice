from fastapi import APIRouter
from starlette import status

from .notif import send_notif
from .schemas import UserLogin


router = APIRouter(tags=["home/"])


@router.post('/sendemail', status_code=status.HTTP_200_OK)
async def send_email(user: UserLogin):
    content = 'User Logged In ...'
    send_notif(user.email, content=content)
    return 'Sending Email =)'
