from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import CommentCreatView, CommentDeleteView, CommentUpdateView


urlpatterns = [
    path("post/<int:pk>/add-comment", CommentCreatView.as_view(), name="add-comment"),
    path("update-comment/<int:pk>", CommentUpdateView.as_view(), name="update-comment"),
    path("delete-comment/<int:pk>", CommentDeleteView.as_view(), name="delete-comment"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
