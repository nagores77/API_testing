from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert
import requests


def test_register_positive():
    email = 'eve.holt@reqres.in'
    password = 'Parol'
    res = api.user_register(email, password)

    assert res.status_code == HTTPStatus.OK
    #Assert.validate_schema(res.status_code)




def test_register_negative():
    email = 'eve.holt@reqres.in'
    password = ''
    res = api.user_register(email, password)
    res.body = res.json()
    assert res.status_code == HTTPStatus.BAD_REQUEST
    Assert.validate_schema(res.body)
    assert res.body["error"] == "Missing password"




