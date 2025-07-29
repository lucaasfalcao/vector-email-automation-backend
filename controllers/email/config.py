"""Tags description to Email API"""

from fastapi import APIRouter

EMAIL = dict(name='Email', description='API to manage email sending and templates.')


tags = [EMAIL]

router = APIRouter()
