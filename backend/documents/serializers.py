# In documents/serializers.py
from rest_framework import serializers
from .models import CollaborationSession, Document, DocumentVersion, UserRoles


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            "id",
            "title",
            "owner",
            "collaborators",
            "is_private",
            "created_at",
            "updated_at",
        ]


class DocumentVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentVersion
        fields = ["id", "document", "version_number", "content", "created_at"]


class CollaborationSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollaborationSession
        fields = "__all__"


class UserRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoles
        fields = "__all__"
