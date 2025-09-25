from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from post.models import Article, Comment
from post.serializers import ArticleSerializer, CommentSerializer
from post.middlewares import is_user_object_own

from utils.decorators import error_handler


class BaseCrudApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    @error_handler
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @error_handler
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @error_handler
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @error_handler
    @is_user_object_own
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @error_handler
    @is_user_object_own
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ArticleAPI(BaseCrudApi):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class CommentAPI(BaseCrudApi):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()