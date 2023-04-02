import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BROKER_URL = os.getenv('BROKER_URL')
    EMAIL_USER = os.getenv('EMAIL_USER')
    EMAIL_SERVER = os.getenv('EMAIL_SERVER')
    PASSWORD = os.getenv('PASSWORD')
    SMTP_SERVER = os.getenv('SMTP_SERVER')
    SMTP_PORT = os.getenv('SMTP_PORT')
    
    CELERY_ROUTES = {
        'worker.send_mail': {'queue': 'send_mail'},
    }
    CELERY_IMPORTS = ['task']
    CELERY_TRACK_STARTED=True