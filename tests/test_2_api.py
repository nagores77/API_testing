from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert
import re


def test_list_users():
    res = api.list_users() # переменная res (объект ответа), api  - объект

    assert res.status_code == HTTPStatus.OK
    Assert.validate_schema(res.json()) # через класс обр-ся к методу и передаем json
    assert res.headers['Cache-Control'] == 'max-age=14400' #макс объем кэша - Проверка заголовка


def test_singe_user_not_found():
    res = api.singe_user_not_found()

    assert res.status_code == HTTPStatus.NOT_FOUND
    Assert.validate_schema(res.json())


def test_single_user():
    res = api.single_user()
    res_body = res.json()

    assert res.status_code == HTTPStatus.OK
    Assert.validate_schema(res_body)
    assert re.fullmatch(r'\w[a-z]{0,6}', res_body["data"]["last_name"])
    print(res_body)


def test_create():    #need to delete created data. Тест дб атомарным: созданную в целях проверки запись н-но удалить по окончании теста
    name = 'Boris'
    job = 'Tester'
    res = api.create(name, job) #ответ из предыдущего запроса

    assert res.status_code == HTTPStatus.CREATED
    assert res.json()['name'] == name
    assert res.json()['job'] == job
    assert re.fullmatch(r'\d{1,4}', res.json()['id'])  #это нормально, что подсвечивает желтым. Посвечиваются все регулярные выр-ния

    assert api.delete_user(res.json()['id']).status_code == HTTPStatus.NO_CONTENT

