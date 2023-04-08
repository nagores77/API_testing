from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert
import requests


def test_register():
    email = 'eve.holt@reqres.in'
    password = 'Parol'
    res = api.create(email, password)

    assert res.status_code == HTTPStatus.CREATED
    assert api.list_users().status_code == HTTPStatus.OK

    assert api.delete_user(res.json()).status_code == HTTPStatus.NO_CONTENT