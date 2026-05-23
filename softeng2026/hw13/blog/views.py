from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.


class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'blog/index.html'
    
class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    
 