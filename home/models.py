from django.db import models

# Create your models here.

# python manage.py makemigrations
# python manage.py migrate
# python manage.py showmigrations
# python manage.py sqlmigrate {앱 이름} {마이그레이션}

class portfolio(models.Model):
    id = models.AutoField(primary_key = True) # 번호
    title = models.CharField(max_length=255) # 제목
    subject = models.CharField(max_length=255) #주제
    field = models.CharField(max_length=100) # 필드
    description = models.CharField(max_length = 500) # 내용
    number= models.IntegerField() # 순서
    video_title = models.CharField(max_length = 500) # 영상제목
    video_url = models.CharField(max_length=255) # 영상
    created_at = models.DateTimeField(auto_now_add=True) #등록일자
    img_path = models.ImageField(upload_to='images/') #이미지

    def __str__(self):
        return self.title