from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm
from django.db.models import F

class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'community/post_form.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(form)

class PostListView(ListView):
    model = Post
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        pk = self.kwargs['pk']
        Post.objects.filter(pk=pk).update(view_count=F('view_count')+1)
        return super().get_object(queryset=queryset)

    

class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'community/post_form.html'

    def test_func(self):
        return self.request.user == self.get_object().author

class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('community:post_list')

    def test_func(self):
        return self.request.user == self.get_object().author

# def apply_possible(request, **kwargs):
#     post = get_object_or_404(Post, pk=request.pk)
#     if post.total_user == post.apply_user:
#         return False
#     return True

# @user_passes_test(apply_possible)
@login_required
def post_apply(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.apply_user.add(request.user)
    redirect_url = request.META.get("HTTP_REFERER", "root")
    return redirect(redirect_url)