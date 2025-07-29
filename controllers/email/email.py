"""Controller for Email"""

from services.gmail import gmail as gmail_service
from .config import EMAIL, router


@router.post(
    path='/email',
    summary='Send a Email to client',
    tags=[EMAIL['name']],
    response_model=str,
)
def send_email(destinatario: str):
    """Send an email to the client"""
    return gmail_service.create_email(destinatario=destinatario)
