#создаем базовый класс (как basic page) - main methods
import requests


class Client:

    @staticmethod  #для их вызова не нужен объект (для статических методов), тк не исп-т self, ему не н-на инициализация
    def get(url, timeout=5):
        return requests.request("GET", url, timeout=timeout)

    @staticmethod
    def post(url, headers, payload, timeout=5):
        return requests.request("POST", url, headers=headers, data=payload, timeout=timeout)

    @staticmethod
    def delete(url, timeout=5):
        return requests.request("DELETE", url, timeout=timeout)


