from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Post
from .filters import PostFilter
from .forms import NewsForm


class PostList(ListView):
    model = Post
    ordering = 'head'
    template_name = 'all_news.html'
    context_object_name = 'all_news'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'


class PostSearch(ListView):
    form_class = NewsForm
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'all_news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('News.add_news',)
    form_class = NewsForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.choice = 'NEWS'
        return super().form_valid(form)


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('News.change_news',)
    form_class = NewsForm
    model = Post
    template_name = 'post_edit.html'


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('News.delete_news',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class ArtsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('News.add_news',)
    form_class = NewsForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.choice = 'NEWS'
        return super().form_valid(form)


class ArtsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('News.change_news',)
    form_class = NewsForm
    model = Post
    template_name = 'post_edit.html'


class ArtsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('News.delete_news',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
