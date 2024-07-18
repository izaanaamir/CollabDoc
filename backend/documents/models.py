from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Document(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="owned_documents",
    )
    collaborators = models.ManyToManyField(
        User, related_name="collaborating_documents", blank=True
    )
    is_private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        is_new = not self.pk
        super().save(*args, **kwargs)

        if is_new:
            DocumentVersion.objects.create(
                document=self, version_number=1.0, content=""
            )

    def add_collaborator(self, user):
        self.collaborators.add(user)

    def remove_collaborator(self, user):
        self.collaborators.remove(user)


class DocumentVersion(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    version_number = models.FloatField(default=1.0)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.document.updated_at = self.created_at
        self.document.save()


class CollaborationSession(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("document", "user")


class UserRoles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=50,
        choices=(("owner", "Owner"), ("collaborator", "Collaborator")),
    )

    class Meta:
        unique_together = ("user", "document")
