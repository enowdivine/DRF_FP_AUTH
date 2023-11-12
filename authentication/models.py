from django.db import models
import jwt
from django.utils import timezone
from datetime import datetime, timedelta
from django.conf import settings


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def token(self):
        jwttoken = jwt.encode(
            {
                "username": self.username,
                "email": self.email,
                "exp": datetime.now(tz=timezone.utc) + timedelta(hours=24),
            },
            settings.SECRET_KEY,
            algorithm="HS256",
        )
        return jwttoken
