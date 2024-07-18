from rest_framework import generics, permissions
from .models import Document, DocumentVersion
from .serializers import DocumentSerializer, DocumentVersionSerializer


class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]


class DocumentVersionListCreateView(generics.ListCreateAPIView):
    serializer_class = DocumentVersionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        document_id = self.kwargs["document_id"]
        return DocumentVersion.objects.filter(document_id=document_id)

    def perform_create(self, serializer):
        document_id = self.kwargs["document_id"]
        document = Document.objects.get(id=document_id)
        version_number = (
            DocumentVersion.objects.filter(document=document).count() + 1
        )
        serializer.save(document=document, version_number=version_number)
