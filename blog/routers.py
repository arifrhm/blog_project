# blog/urls.py
from rest_framework import routers
from .views import ArticleViewSet, EditorProfileViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'editors', EditorProfileViewSet)

urlpatterns = router.urls
