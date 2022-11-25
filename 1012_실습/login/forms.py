from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class loginForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ("username",)
        label = {
            'username' : '아이디',
        }

#여기서 label 은 무시하고 UserCreationForm 이란 form을 사용할거고 class 이름(UsercreationForm):
# UsercreationForm 내부에 class Meta: 정의되어있지만 여기서 저희가 직접 다뤄서
# model 은 저희가 .model 에서 직접 만든 모델 User을 사용
# fields = '__all__' 해보면 여러 값들이있는데 그 중 username Form만 가져오기 때문에 username만