from rest_framework import generics, permissions
from .models import CollaborationSession, Document, DocumentVersion, UserRoles
from .serializers import (
    CollaborationSessionSerializer,
    DocumentSerializer,
    DocumentVersionSerializer,
    UserRolesSerializer,
)
from django.contrib.auth import get_user_model

User = get_user_model()


class DocumentListCreateView(generics.ListCreateAPIView):
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Document.objects.filter(owner=user) | Document.objects.filter(
            collaborators=user
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        instance = self.get_object()
        collaborators = self.request.data.get("collaborators", [])
        for collaborator_id in collaborators:
            collaborator = User.objects.get(id=collaborator_id)
            instance.add_collaborator(collaborator)
        serializer.save()


class DocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        document_id = self.kwargs["document_id"]
        return Document.objects.filter(id=document_id)


class DocumentVersionListCreateView(generics.ListCreateAPIView):
    serializer_class = DocumentVersionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        document_id = self.kwargs["document_id"]
        return DocumentVersion.objects.filter(document_id=document_id)

    def perform_create(self, serializer):
        document_id = self.kwargs["document_id"]
        document = Document.objects.get(id=document_id)
        latest_version = document.versions.first()
        new_version_number = (
            latest_version.version_number + 0.1 if latest_version else 1.0
        )
        serializer.save(document=document, version_number=new_version_number)
        document.save()


class DocumentVersionDetailView(generics.RetrieveAPIView):
    serializer_class = DocumentVersionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        document_id = self.kwargs["document_id"]
        version_id = self.kwargs["version_id"]
        return DocumentVersion.objects.filter(
            document__id=document_id, id=version_id
        )


class CollaborationSessionListView(generics.ListCreateAPIView):
    queryset = CollaborationSession.objects.all()
    serializer_class = CollaborationSessionSerializer


class UserRolesListView(generics.ListCreateAPIView):
    queryset = UserRoles.objects.all()
    serializer_class = UserRolesSerializer
