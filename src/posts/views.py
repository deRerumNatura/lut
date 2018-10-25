from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.conf import settings

from .models import Posts
from .forms import PostForm


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
        obj = form.save(commit=False) # todo Спросить
        obj.author = self.request.user
        return super(PostsCreateView, self).form_valid(form)