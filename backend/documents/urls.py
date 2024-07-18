from django.urls import path
from .views import (
    CollaborationSessionListView,
    DocumentListCreateView,
    DocumentDetailView,
    DocumentVersionListCreateView,
    DocumentVersionDetailView,
    UserRolesListView,
)

urlpatterns = [
    path("", DocumentListCreateView.as_view(), name="document_list_create"),
    path(
        "<int:document_id>/",
        DocumentDetailView.as_view(),
        name="document_detail",
    ),
    path(
        "<int:document_id>/versions/",
        DocumentVersionListCreateView.as_view(),
        name="document_version_list_create",
    ),
    path(
        "documents/<int:document_id>/versions/<int:version_id>/",
        DocumentVersionDetailView.as_view(),
        name="document_version_detail",
    ),
    path(
        "collaboration-sessions/",
        CollaborationSessionListView.as_view(),
        name="collaboration-session-list",
    ),
    path(
        "user-roles/",
        UserRolesListView.as_view(),
        name="user-roles-list",
    ),
]
