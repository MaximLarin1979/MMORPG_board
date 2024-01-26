from django.contrib.auth.models import User
from .models import Category, Post, Reply
from django.views.generic import ListView, DetailView, CreateView, UpdateView


class PostsList(ListView):
    model = Post
    template_name = 'posts_template.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_logged'] = self.request.user.is_authenticated
        context['current_user'] = self.request.user
        context['user_is_staff'] = self.request.user.is_staff
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail_template.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        replies_by_post_id = Reply.objects.filter(post=self.kwargs['pk']).order_by('-date_posted')
        context['is_logged'] = self.request.user.is_authenticated
        context['replys'] = replies_by_post_id
        return context
