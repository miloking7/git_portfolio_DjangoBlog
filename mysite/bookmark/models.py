from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Bookmark(models.Model):
    #묵시적으로 아이디가 프라이머리키로 자동증가되는 필드가 만들어진다
    title = models.CharField('TITLE',max_length=100,blank=True,)
    url = models.URLField('URL',unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.title 