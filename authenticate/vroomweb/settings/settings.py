from .base import *


STATIC_ROOT = os.path.join(BASE_DIR, 'extras/www/static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'extras/www/media')
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'extras/www/assets') ]


CSRF_TRUSTED_ORIGINS = [
    "https://payglex.co.za",
    "https://www.payglex.co.za", 
    "https://*.payglex.co.za", 
    "https://*.ngrok-free.app",
    "https://www.example.com",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]


EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = config("EMAIL_USE_TLS")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")
DEFAULT_FROM_ADMIN = config("DEFAULT_FROM_ADMIN")

RABBITMQ = {
    'default': {
        'host': 'localhost',
        'port': 5672,
        # 'user': 'guest',
        'username': 'guest',
        'password': 'guest',
        # 'virtual_host': '/'
    },
}