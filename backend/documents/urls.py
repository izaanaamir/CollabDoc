from django.urls import path
from .views import (
    DocumentListCreateView,
    DocumentDetailView,
    DocumentVersionListCreateView,
)

urlpatterns = [
    path("", DocumentListCreateView.as_view(), name="document_list_create"),
    path("<int:pk>/", DocumentDetailView.as_view(), name="document_detail"),
    path(
        "<int:document_id>/versions/",
        DocumentVersionListCreateView.as_view(),
        name="document_version_list_create",
    ),
]
