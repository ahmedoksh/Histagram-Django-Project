from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView, UpdateView, ListView
from .models import Profile
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.


def SignUp(request):
    '''This function is used to register a new user
    The function checks if the request method is POST, if it is POST, it will create a new user
    and redirect to login page, if it is GET, it will render the register page
    '''
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def LogOut(request):
    '''This function is used to logout the current login user and redirect to login page'''
    logout(request)
    return redirect("login")


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "users/profile.html"


class ProfileUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    model = Profile
    template_name = "users/profile_update.html"
    fields = ["picture", "name", "status"]

    def test_func(self):
        '''This function is used to check if the current login user is the author of the profile we are trying to update
        Returns:
            (bool): True if the current login user is the author of the profile, False otherwise
        '''
        profile = self.get_object()  # that gets the profile that we are trying to update
        if (self.request.user == profile.user):  
            return True
        return False

    def get_success_url(self):
        profile_id = self.object.id
        return reverse("profile", kwargs={"pk": profile_id})

    success_message = "Your profile has been updated"


class SearchProfileView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = "users/search.html"

    def get_queryset(self): 
        '''This function is used to search for a profile by name or username'''
        query = self.request.GET.get("q")

        object_list = Profile.objects.filter(
            Q(name__icontains=query) | Q(user__username__icontains=query)
        )
        return object_list
