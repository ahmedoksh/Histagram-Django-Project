from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ProfileDetailView, ProfileUpdateView, SearchProfileView
from .views import SignUp, LogOut
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("signup/", SignUp, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),  # template_name'xx' tells it where to find the log in url
    path("logout/", LogOut, name="logout"),
    path("<int:pk>/profile", ProfileDetailView.as_view(), name="profile"),
    path("<int:pk>/profile/update", ProfileUpdateView.as_view(), name="update-profile"),
    path("profile/search", SearchProfileView.as_view(), name="search-profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
