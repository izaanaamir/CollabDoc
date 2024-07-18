# In documents/serializers.py
from rest_framework import serializers
from .models import Document, DocumentVersion


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            "id",
            "title",
            "owner",
            "is_private",
            "created_at",
            "updated_at",
        ]


class DocumentVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentVersion
        fields = ["id", "document", "version_number", "content", "created_at"]
