from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app)
    response = client.get('/')
    assert response.json() == {'message': 'Olá, mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_root_html_deve_retornar_ola_mundo_em_html():
    client = TestClient(app)
    response = client.get('/html')
    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text
