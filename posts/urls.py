from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PostsListView, PostCreatView, PostDeleteView, PostDetailView

urlpatterns = [
    path("", PostsListView.as_view(), name="homepage"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="delete-post"),
    path("creat-post", PostCreatView.as_view(), name="create-post"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="detail-post"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
