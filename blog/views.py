# blog/views.py
from rest_framework import viewsets, permissions
from .models import Article, EditorProfile
from .serializers import ArticleSerializer, EditorProfileSerializer
from .permissions import IsEditorOrAdmin


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [
                permissions.IsAuthenticated, IsEditorOrAdmin
                ]
        else:
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()


class EditorProfileViewSet(viewsets.ModelViewSet):
    queryset = EditorProfile.objects.all()
    serializer_class = EditorProfileSerializer
