"""Controller for Email"""

from fastapi import Body
from services.gmail import gmail as gmail_service
from .config import EMAIL, router


@router.post(
    path='/email',
    summary='Send a Email to client',
    tags=[EMAIL['name']],
    response_model=str,
)
def send_email(
    recipients: list[str] = Body(
        description='List of email recipients',
        example=['email@gmail.com']
    ),
) -> str:
    """Send an email to the client"""
    return gmail_service.create_email(recipients=recipients)
