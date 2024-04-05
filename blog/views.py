from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Category, Tag

# Create your views here.
class PostList(ListView) :
    model = Post
    # template_name = 'blog/post_list.html' # CBV를 사용시 템플릿 이름 강제 지정
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        # 모든 카테고리를 가져와 categories 키에 연결해 담기
        context['categories'] = Category.objects.all()
        # category가 없는 post 카운트해서 no_categories.... 키에 연결해 담기
        context['no_category_post_count'] = Post.objects.filter(category=None).count()

        return context

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']

class PostDetail(DetailView) :
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        # 모든 카테고리를 가져와 categories 키에 연결해 담기
        context['categories'] = Category.objects.all()
        # category가 없는 post 카운트해서 no_categories.... 키에 연결해 담기
        context['no_category_post_count'] = Post.objects.filter(category=None).count()

        return context

def category_page(request, slug) :
    if slug == 'no_category' :
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else :
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list' : post_list,
            'categories' : Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count(),
            'category' : category
        }
    )

def tag_page(request, slug) :
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list' : post_list,
            'tag' : tag,
            'catergories' : Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count(),
        }
    )
#  def index(request) :
#     posts = Post.objects.all().order_by('-pk')   # 모든값들을 PK값 기준으로 정렬하여 posts에 저장
#     return render(request, 'blog/post_list.html',
#                     {
#                       'posts' : posts
#                   }
#                   )

# def single_post_page(request, pk) :
#     post = Post.objects.get(pk=pk)
#     return render(request, 'blog/post_detail.html',
#                   {
#                       'post' : post,
#                   }
#                   )

