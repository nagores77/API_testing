from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert
import requests


def test_register_positive():
    email = 'eve.holt@reqres.in'
    password = 'Parol'
    res = api.create(email, password)

    #assert res.status_code == HTTPStatus.CREATED
    assert api.list_users().status_code == HTTPStatus.OK

    assert api.delete_user(res.json()).status_code == HTTPStatus.NO_CONTENT


def test_register_negative():
    email = 'eve.holt@reqres.in'
    password = ''
    res = api.user_register(email, password)
    res.body = res.json()
    assert res.status_code == HTTPStatus.BAD_REQUEST
    Assert.validate_schema(res.body)
    assert res.body["error"] == "Missing password"


    #assert api.delete_user(res.json()).status_code == HTTPStatus.NO_CONTENT

