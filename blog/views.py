from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
class PostList(ListView) :
    model = Post
    # template_name = 'blog/post_list.html' # CBV를 사용시 템플릿 이름 강제 지정
    ordering = '-pk'

#  def index(request) :
#     posts = Post.objects.all().order_by('-pk')   # 모든값들을 PK값 기준으로 정렬하여 posts에 저장
#     return render(request, 'blog/post_list.html',
#                     {
#                       'posts' : posts
#                   }
#                   )
def single_post_page(request, pk) :
    post = Post.objects.get(pk=pk)

    return render(request, 'blog/single_post_page.html',
                  {
                      'post' : post,
                  }
                  )