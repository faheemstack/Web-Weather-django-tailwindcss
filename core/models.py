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


class CustomUser(models.Model):

    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)

    profile_image = models.ImageField(upload_to='profiles/')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

