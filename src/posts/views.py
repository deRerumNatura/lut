from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Posts


class PostsListView(ListView):
    model = Posts


class PostsDetailView(DetailView):
    model = Posts
