from django.db import models
from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()



# Create your models here.
def get_db():
    URI = os.getenv('MONGO_URI')
    db_name  = os.getenv('MONGO_DB_NAME')
    client  = MongoClient(URI)
    db  = client[db_name]
    return db

