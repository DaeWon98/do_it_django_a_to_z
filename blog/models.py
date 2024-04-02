from django.db import models

class Post(models.Model) :
    title = models.CharField(max_length=30) # 문자를 담는 필드 생성 (최대길이 50)
    content = models.TextField() # 문자열의 길이 제한없는 TextField를 사용해 본문필드 생성

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/',
                                   blank=True)

    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d',
                                   blank=True)

    created_at = models.DateTimeField(auto_now_add=True) # 시간 데이터 기록
    update_at = models.DateTimeField(auto_now=True)

    # 게시글의 PK값과 제목을 반환
    def __str__(self) :
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self) :
        return (f'/{self.pk}/')