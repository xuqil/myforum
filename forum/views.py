from django.shortcuts import render
from django.views.generic import ListView

from .models import Topic


class IndexView(ListView):
    """
    首页
    """
    template_name = 'index.html'
    context_object_name = 'topics'
    model = Topic

