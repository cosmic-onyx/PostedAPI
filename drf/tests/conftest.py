import pytest

from django.contrib.auth.models import User
from django.conf import settings

from rest_framework.test import APIClient
from ninja_jwt.tokens import AccessToken

from post.models import Category, Article, Comment


@pytest.fixture
def user(db):
    return User.objects.create_user(username='user1', password='pwd1')


@pytest.fixture
def category(db):
    return Category.objects.create(category='news')


@pytest.fixture
def client_auth(user):
    api = APIClient()
    token = AccessToken.for_user(user)
    api.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return api


@pytest.fixture
def client_anon():
    return APIClient()


@pytest.fixture
def client():
    # Django test client for non-DRF endpoints (e.g., Ninja auth)
    from django.test import Client as DjangoClient
    return DjangoClient()


@pytest.fixture(autouse=True)
def allow_testserver_host():
    settings.ALLOWED_HOSTS = ['testserver', 'localhost', '127.0.0.1']
    return settings


@pytest.fixture
def article(user, category):
    return Article.objects.create(user=user, category=category, title='T', content='C')


@pytest.fixture
def comment(user, article):
    return Comment.objects.create(user=user, article=article, content='Nice')