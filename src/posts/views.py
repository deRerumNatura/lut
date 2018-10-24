from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Posts
from .forms import PostForm


class PostsListView(ListView):
    model = Posts


class PostsDetailView(DetailView):
    model = Posts


class PostsCreateView(CreateView):
    form_class = PostForm
    template_name = "form.html"
    success_url = '/'