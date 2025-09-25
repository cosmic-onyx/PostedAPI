import pytest


ARTICLES = 'http://127.0.0.1:8000/api/v1/article/'
COMMENTS = 'http://127.0.0.1:8000/api/v1/comment/'


@pytest.mark.django_db
def test_article_create_success(client_auth, user, category):
    payload = {
        'category_id': category.id,
        'title': 'test',
        'content': 'test2'
    }
    resp = client_auth.post(ARTICLES, data=payload, format='json')
    assert resp.status_code in (200, 201)
    assert resp.data['title'] == 'test'


@pytest.mark.django_db
def test_article_create_fail_unauthorized(client_anon):
    resp = client_anon.post(ARTICLES, data={})
    assert resp.status_code in (401, 403)


@pytest.mark.django_db
def test_article_read_success(client_auth, article):
    resp = client_auth.get(f'{ARTICLES}{article.id}/')
    assert resp.status_code == 200
    assert resp.data['id'] == article.id


@pytest.mark.django_db
def test_article_read_fail_unauthorized(client_anon, article):
    resp = client_anon.get(f'{ARTICLES}{article.id}/')
    assert resp.status_code in (401, 403)


@pytest.mark.django_db
def test_article_update_success(client_auth, user, category, article):
    payload = { 'title': 't2', 'content': 'c2', 'category_id': category.id }
    resp = client_auth.put(f'{ARTICLES}{article.id}/', data=payload, format='json')
    assert resp.status_code in (200, 202)


@pytest.mark.django_db
def test_article_update_fail_unauthorized(client_anon, article):
    resp = client_anon.put(f'{ARTICLES}{article.id}/', data={'title': 'test'})
    assert resp.status_code in (401, 403)


@pytest.mark.django_db
def test_article_delete_success(client_auth, article):
    resp = client_auth.delete(f'{ARTICLES}{article.id}/')
    assert resp.status_code in (200, 202, 204)


@pytest.mark.django_db
def test_article_delete_fail_unauthorized(client_anon, article):
    resp = client_anon.delete(f'{ARTICLES}{article.id}/')
    assert resp.status_code in (401, 403)


@pytest.mark.django_db
def test_comment_create_success(client_auth, user, article):
    payload = { 'article_id': article.id, 'content': 'test' }
    resp = client_auth.post(COMMENTS, data=payload, format='json')
    assert resp.status_code in (200, 201)
    assert resp.data['content'] == 'test'


@pytest.mark.django_db
def test_comment_create_fail_unauthorized(client_anon, article):
    resp = client_anon.post(COMMENTS, data={'article_id': article.id, 'content': 'test'})
    assert resp.status_code in (401, 403)


@pytest.mark.django_db
def test_comment_read_success(client_auth, comment):
    resp = client_auth.get(f'{COMMENTS}{comment.id}/')
    assert resp.status_code == 200
    assert resp.data['id'] == comment.id


@pytest.mark.django_db
def test_comment_read_fail_unauthorized(client_anon, comment):
    resp = client_anon.get(f'{COMMENTS}{comment.id}/')
    assert resp.status_code in (401, 403)


@pytest.mark.django_db
def test_comment_update_success(client_auth, user, article, comment):
    payload = { 'article_id': article.id, 'content': 'Edited' }
    resp = client_auth.put(f'{COMMENTS}{comment.id}/', data=payload, format='json')
    assert resp.status_code in (200, 202)


@pytest.mark.django_db
def test_comment_update_fail_unauthorized(client_anon, comment):
    resp = client_anon.put(f'{COMMENTS}{comment.id}/', data={'content': 'X'})
    assert resp.status_code in (401, 403)


@pytest.mark.django_db
def test_comment_delete_success(client_auth, comment):
    resp = client_auth.delete(f'{COMMENTS}{comment.id}/')
    assert resp.status_code in (200, 202, 204)


@pytest.mark.django_db
def test_comment_delete_fail_unauthorized(client_anon, comment):
    resp = client_anon.delete(f'{COMMENTS}{comment.id}/')
    assert resp.status_code in (401, 403)

