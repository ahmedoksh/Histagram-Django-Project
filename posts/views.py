from .models import Posts
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
)
from django.urls import reverse_lazy

# Create your views here.


class PostsListView(LoginRequiredMixin, ListView):
    model = Posts
    template_name = "posts/list.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


class PostCreatView(LoginRequiredMixin, CreateView):
    model = Posts
    fields = ["image", "caption"]
    template_name = "posts/create.html"
    success_url = reverse_lazy("homepage")
    success_message = "Your post has been created"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    model = Posts
    success_url = reverse_lazy("homepage")
    template_name = "posts/delete.html"
    success_message = "Your post has been deleted"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Posts
    template_name = "posts/detail.html"
