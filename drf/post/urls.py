from django.urls import path, include
from rest_framework.routers import DefaultRouter

from post.views import ArticleAPI, CommentAPI


router = DefaultRouter()

router.register(r'article', ArticleAPI, basename='article')
router.register(r'comment', CommentAPI, basename='comment')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]