from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(models.Model): # Model을 상속받는다
# 	name = models.CharField(max_length=20) # 짧은 문장
# 	description = models.TextField() # 긴 텍스트 문장
# 	age = models.PositiveIntegerField(null=True) # 양의 정수형 숫자 
# 	gender = models.CharField(max_length=10)

# 	def __str__(self):
# 		return f"{self.name} / ({self.age}살) / {self.gender}"

class User(AbstractUser):
    is_business = models.BooleanField(default=False)
    grade = models.CharField(max_length=10, default='C')