from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 시간정보 자동 등록(글 쓰기 할 때 '어제 등록했어' X처럼)