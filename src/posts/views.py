from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Posts, Likes
from .forms import PostForm


def like(request):
    post_to_like = Posts.objects.filter(id=request.POST['post_id']).get()
    is_liked = Likes.objects.filter(author=request.user, post_id=post_to_like)

    if not is_liked:
        Likes.objects.create(author=request.user, post=post_to_like)

    return redirect('/')


class PostsListView(ListView):
    model = Posts

    def get_queryset(self):
        return Posts.objects.filter(author=self.request.user)


class PostsDetailView(DetailView):
    model = Posts

    def get_queryset(self):
        return Posts.objects.filter(author=self.request.user)


class PostsCreateView(CreateView):
    form_class = PostForm
    template_name = "form.html"
    success_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False) # todo что приходит в obj? данный с формы?
        obj.author = self.request.user
        return super(PostsCreateView, self).form_valid(form)


class PostUpdateView(UpdateView):
    form_class = PostForm
    template_name = "form.html"
    success_url = '/'

    def get_queryset(self):
        return Posts.objects.filter(author=self.request.user)