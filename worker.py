from celery import Celery
from flask import Flask
from config import Config

def create_worker():
    _celery = Celery(__name__, broker=Config.BROKER_URL)
    _celery.conf.update(Config.__dict__)
    return _celery

worker = create_worker()