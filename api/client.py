#создаем базовый класс (как basic page)
import requests


class Client:

    @staticmethod  #для их вызова не нужен объект (для статических методов), тк не исп-т self, ему не н-на инициализация
    def get(url):
        return requests.request("GET", url)

    @staticmethod
    def post(url, headers, payload):
        return requests.request("POST", url, headers=headers, data=payload)

    @staticmethod
    def delete(url):
        return requests.request("DELETE", url)
