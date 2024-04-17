from django.db import transaction,models

# Create your models here.

# python manage.py makemigrations
# python manage.py migrate
# python manage.py showmigrations
# python manage.py sqlmigrate {앱 이름} {마이그레이션}

class Portfolio(models.Model):
    FIELD_CHOICES = (
        (1,'기업홍보'),
        (2,'제품홍보'),
        (3,'브이로그'),
    )
    id = models.AutoField(primary_key = True) # 번호(화면에 안보임)
    number = models.IntegerField(blank=True, null=True)  # 순서를 위한 필드
    field = models.IntegerField(choices=FIELD_CHOICES)  # 필드
    title = models.CharField(max_length=255) # 제목
    description = models.CharField(max_length = 500) # 내용
    video_url = models.CharField(max_length=255) # 영상
    img_path = models.ImageField(upload_to='images/') #이미지
    created_at = models.DateTimeField(auto_now_add=True) #등록일자

    class Meta:
        ordering = ['number', 'created_at']  # number로 주로 정렬하되, 동일한 경우 created_at으로 정렬


    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self.number is None:
                last_number = Portfolio.objects.select_for_update().aggregate(models.Max('number'))['number__max']
                self.number = (last_number or 0) + 1
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title