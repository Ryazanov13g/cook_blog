from django.views.generic import ListView, DetailView, CreateView

from blog.models import Post, Comment
from blog.forms import CommentForm
from common.views import TitleMixin


class HomeView(TitleMixin, ListView):
    model = Post
    paginate_by = 5
    template_name = 'blog/home.html'
    title = 'Foodeiblog | Главная'


class PostListView(TitleMixin, ListView):
    model = Post
    title = 'Foodeiblog | Посты'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')


class PostDetailView(TitleMixin, DetailView):
    model = Post
    slug_url_kwarg = 'post_slug'
    title = 'Foodeiblog | Пост'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()
