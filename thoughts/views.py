from django.shortcuts import render

from thoughts.models import Blog, Category, Profile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

from random import choice
from string import ascii_lowercase, ascii_uppercase, digits

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView

from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login'] = AuthenticationForm
        return context


class UserCreateView(FormView):
    template_name = "auth/user_form.html"
    model = User
    form_class = UserCreationForm
    # success_url = reverse_lazy('index_view')

    def get_success_url(self, **kwargs):
      return reverse_lazy('profile_create_view')

    # Had to look this up on StackOverflow
    def form_valid(self, form):
      #save the new user first
      form.save()
      #get the username and password
      username = self.request.POST['username']
      password = self.request.POST['password1']
      #authenticate user then login
      user = authenticate(username=username, password=password)
      login(self.request, user)
      return super(UserCreateView, self).form_valid(form)

class CategoryCreateView(CreateView):
    model = Category
    fields = ('title', )
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.random_url = ''
        for i in range(20):
            instance.random_url += choice(ascii_lowercase + ascii_uppercase + digits)
        return super().form_valid(form)

class ProfileCreateView(CreateView):
    model = Profile
    fields = ('first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.random_url = ''
        for i in range(5):
            instance.random_url += choice(ascii_lowercase + ascii_uppercase + digits)
        instance.random_url += self.request.user.profile.first_name[0:3]
        for i in range(5):
            instance.random_url += choice(ascii_lowercase + ascii_uppercase + digits)
        instance.random_url += self.request.user.profile.first_name[3:]
        for i in range(5):
            instance.random_url += choice(ascii_lowercase + ascii_uppercase + digits)
        return super().form_valid(form)

class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ('first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.random_url = ''
        for i in range(5):
            instance.random_url += choice(ascii_lowercase + ascii_uppercase + digits)
        instance.random_url += self.request.user.profile.first_name[0:3]
        for i in range(5):
            instance.random_url += choice(ascii_lowercase + ascii_uppercase + digits)
        instance.random_url += self.request.user.profile.first_name[3:]
        for i in range(5):
            instance.random_url += choice(ascii_lowercase + ascii_uppercase + digits)
        return super().form_valid(form)

class CategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(user=self.request.user)
        return context
