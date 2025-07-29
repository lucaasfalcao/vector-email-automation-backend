"""Creation of controller list"""

from . import email

routes = [
    email.router,
]

tags = [
    *email.tags,
]
