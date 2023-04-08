from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert


def test_list_users():
    res = api.list_users() # переменная res (объект ответа), api  - объект

    assert res.status_code == HTTPStatus.OK
    Assert.validate_schema(res.json()) # через класс обр-ся к методу и передаем json


def test_singe_user_not_found():
    res = api.singe_user_not_found()

    assert res.status_code == HTTPStatus.NOT_FOUND
    Assert.validate_schema(res.json())


def test_single_user():
    res = api.single_user()
    res_body = res.json()

    assert res.status_code == HTTPStatus.OK
    Assert.validate_schema(res_body)


def test_create():    #need to delete created data. Тест дб атомарным: созданную в целях проверки запись н-но удалить по окончании теста
    name = 'Boris'
    job = 'Tester'
    res = api.create(name, job) #ответ из предыдущего запроса

    assert res.status_code == HTTPStatus.CREATED
    assert res.json()['name'] == name
    assert res.json()['job'] == job

    assert api.delete_user(res.json()['id']).status_code == HTTPStatus.NO_CONTENT

