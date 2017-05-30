from django.shortcuts import render

from thoughts.models import Blog, Category, Profile, Reply

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

from random import choice
from string import ascii_lowercase, ascii_uppercase, digits

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView

from django.urls import reverse_lazy, reverse

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
    success_url = reverse_lazy('category_list_view')

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

class CategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.filter(user=self.request.user)
        return context

class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['details'] = Category.objects.filter(id=self.kwargs['pk'])
        return context

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('title', )
    # success_url = reverse_lazy('category_list_view')
    def get_success_url(self, *args, **kwargs):
        x = Category.objects.get(id=self.kwargs['pk']).id
        y = Category.objects.get(random_url=self.kwargs['random_url']).random_url
        return reverse('category_detail_view', args=[y, x])

class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'text')
    # success_url = reverse_lazy('category_list_view')

    def get_success_url(self, *args, **kwargs):
        x = Category.objects.get(id=self.kwargs['pk']).id
        y = Category.objects.get(random_url=self.kwargs['random_url']).random_url
        return reverse('category_detail_view', args=[y, x])

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.writer = self.request.user
        instance.category = Category.objects.get(id=self.kwargs['pk'])
        instance.random_url = ''
        for i in range(20):
            instance.random_url += choice(ascii_lowercase + ascii_uppercase + digits)
        return super().form_valid(form)

class BlogDetailView(DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Blog.objects.filter(id=self.kwargs['pk'])
        return context

class BlogTextUpdateView(UpdateView):
    model = Blog
    fields = ('text', )
    # success_url = reverse_lazy('category_list_view')
    def get_success_url(self, *args, **kwargs):
        x = Blog.objects.get(id=self.kwargs['pk']).id
        y = Blog.objects.get(random_url=self.kwargs['random_url']).random_url
        return reverse('blog_detail_view', args=[y, x])

class BlogTitleUpdateView(UpdateView):
    model = Blog
    fields = ('title', )
    # success_url = reverse_lazy('category_list_view')
    def get_success_url(self, *args, **kwargs):
        x = Blog.objects.get(id=self.kwargs['pk']).id
        y = Blog.objects.get(random_url=self.kwargs['random_url']).random_url
        return reverse('blog_detail_view', args=[y, x])

class ReplyCreateView(CreateView):
    model = Reply
    fields = ('text', )
    # success_url = reverse_lazy('category_list_view')
    def get_success_url(self, *args, **kwargs):
        x = Blog.objects.get(id=self.kwargs['pk']).id
        y = Blog.objects.get(random_url=self.kwargs['random_url']).random_url
        return reverse('blog_detail_view', args=[y, x])

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.writer = self.request.user
        instance.blog = Blog.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

class ReplyUpdateView(UpdateView):
    model = Reply
    fields = ('text', )
    # success_url = reverse_lazy('category_list_view')
    def get_success_url(self, *args, **kwargs):
        x = Reply.objects.get(id=self.kwargs['pk']).blog.id
        y = Reply.objects.get(id=self.kwargs['pk']).blog.random_url
        return reverse('blog_detail_view', args=[y, x])
