from django.db import models
import os
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown

class Tag(models.Model) :
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True) # 사람이 읽을 수 있는 문자로 고유 URL 생성

    def __str__(self) :
        return self.name

    def get_absolute_url(self) :
        return (f'/blog/tag/{self.slug}/')

class Category(models.Model) :
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True) # 사람이 읽을 수 있는 문자로 고유 URL 생성

    def __str__(self) :
        return self.name

    def get_absolute_url(self) :
        return (f'/blog/category/{self.slug}/')

class Post(models.Model) :
    title = models.CharField(max_length=30) # 문자를 담는 필드 생성 (최대길이 50)
    hook_text = models.CharField(max_length=100, blank=True) # 요약문 필드 생성 제한 글자 100 설정
    content = MarkdownxField() # 문자열의 길이 제한없는 TextField를 사용해 본문필드 생성

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/',
                                   blank=True)

    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d',
                                   blank=True)

    created_at = models.DateTimeField(auto_now_add=True) # 시간 데이터 기록
    update_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.SET_NULL) # Post모델에 category 필드 추가

    tags = models.ManyToManyField(Tag, blank=True)  # ManytoMany는 Null 값을 허용하지 않는다.

    # 게시글의 PK값과 제목을 반환
    def __str__(self) :
        return f'[{self.pk}] {self.title} :: {self.author}'

    def get_absolute_url(self) :
        return (f'/blog/{self.pk}/')

    def get_file_name(self) :
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self) :
        return self.get_file_name().split('.')[-1]

    def get_context_markdown(self):
        return markdown(self.content)