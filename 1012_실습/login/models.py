from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


# User이란 class에서 AbstractUser을 사용한 이유는 settings.py 에서 AUTH_USER_MODEL = 'login.User' 정의한 AUTH_USER_MODEL 을 받아오기 때문에
# models.py 에서 auth.models 의 AbstractUser 를 class User(여기에 넣습니다.) // class User(models.Model) 이건 저희가 모델 직접 만드는 거