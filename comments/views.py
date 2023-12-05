from .models import Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy


# Create your views here.
class CommentCreatView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ["text"]
    template_name = "comments/create.html"
    success_message = "Your comment has been added"
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        '''
        This function adds the current login user and post's information to comment 
        and check if the post id is valid
        '''
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

    def get_success_url(self):
        '''This function is used to redirect to the post detail page after creating the comment'''
        post_id = self.object.post.id
        return reverse("detail-post", kwargs={"pk": post_id})


class CommentDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    model = Comment
    success_message = (
        "Your comment has been deleted" 
    )
    success_url = reverse_lazy("homepage")
    template_name = "comments/delete.html"

    def test_func(self):
        '''
        This function is called before deleting comment to check if the current 
        login user is the author of the post we are trying to delete
        '''
        comment = self.get_object()
        if (self.request.user == comment.user):
            return True
        return False


class CommentUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):  # UserPassesTestMixin makes the user make sure the user pass test condition
    model = Comment
    fields = ["text"]
    template_name = "comments/update.html"
    success_url = reverse_lazy("homepage")
    success_message = "Your post has been updated"

    def test_func(self):
        '''
        This function is used to check if the current login user is the author of the post we are trying to update
        Returns:
            bool: returns True if the current login user is the author of the post we are trying to update
        '''
        comment = self.get_object()
        if (self.request.user == comment.user):
            return True
        return False

    def get_success_url(self):
        '''This function is used to redirect to the post detail page after updating the comment'''
        post_id = self.object.post.id
        return reverse("detail-post", kwargs={"pk": post_id})
