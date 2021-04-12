from django import forms
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .models import Vehicle

class HomePageView(ListView):
    template_name = 'home.html'
    model = Records