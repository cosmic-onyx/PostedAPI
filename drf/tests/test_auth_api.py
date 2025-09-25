import json
import pytest


URL_LOGIN = 'http://127.0.0.1:8000/auth/login'
URL_REGISTER = 'http://127.0.0.1:8000/auth/register'


def cookie_from(resp, name='access_token'):
    for morsel in resp.cookies.values():
        if morsel.key == name:
            return f"{name}={morsel.value}"

    return None


@pytest.mark.django_db
def test_register_success(client):
    resp = client.post(
        URL_REGISTER,
        data=json.dumps({'username': 'user2', 'password': 'pwd2'}),
        content_type='application/json'
    )

    assert resp.status_code in (200, 201)
    assert 'id' in resp.json()
    assert cookie_from(resp) is not None


@pytest.mark.django_db
def test_register_fail_existing_user(client, user):
    resp = client.post(
        URL_REGISTER,
        data=json.dumps({'username': 'user1', 'password': 'pwd1'}),
        content_type='application/json'
    )

    assert resp.status_code == 400


@pytest.mark.django_db
def test_login_success(client, user):
    resp = client.post(
        URL_LOGIN,
        data=json.dumps({'username': 'user1', 'password': 'pwd1'}),
        content_type='application/json'
    )

    assert resp.status_code == 200
    assert cookie_from(resp) is not None


@pytest.mark.django_db
def test_login_fail_bad_credentials(client):
    resp = client.post(
        URL_LOGIN,
        data=json.dumps({'username': 'test', 'password': 'bad'}),
        content_type='application/json'
    )

    assert resp.status_code in (400, 401)