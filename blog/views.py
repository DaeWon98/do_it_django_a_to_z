from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request) :
    posts = Post.objects.all().order_by('-pk')   # 모든값들을 PK값 기준으로 정렬하여 posts에 저장
    return render(request, 'blog/index.html',
                    {
                      'posts' : posts
                  }
                  )

def single_post_page(request, pk) :
    post = Post.objects.get(pk=pk)

    return render(request, 'blog/single_post_page.html',
                  {
                      'post' : post,
                  }
                  )