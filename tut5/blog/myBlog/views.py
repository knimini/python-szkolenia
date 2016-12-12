from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from myBlog.models import *

# Create your views here.


class ListujPosty(ListView):
    model = Post
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['object_list'] = context['object_list'].filter(text__contains="To")
        context['data'] = "2015"
        return context



class DodajPost(CreateView):
    model = Post
    template_name = "create.html"
    fields = ['author', 'title', 'text', 'date']
    success_url = "/"
