from api.httpbin_api import http_bin_api
from http import HTTPStatus
import requests
import re
from utils.assertions import Assert

def test_list_html():

    res = http_bin_api.list_html()
    assert res.status_code == HTTPStatus.OK
    assert res.headers['Content-Type'] == 'text/html; charset=utf-8'

def test_robots():
    #url = 'https://httpbin.org/robots.txt'
    #res = requests.get(url)
    res = http_bin_api.robots_txt()
    assert res.status_code == HTTPStatus.OK
    assert res.headers['Content-Type'] == 'text/plain'

    assert re.fullmatch(r'.*User-agent: \*.*Disallow: /deny.*', res.text, flags=re.DOTALL)


def test_ip():
    res = http_bin_api.check_ip()
    assert res.status_code == HTTPStatus.OK
    assert res.headers['Content-Type'] == 'application/json'
    origin = res.json()["origin"]

    assert re.fullmatch(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', origin)


#'\*' - точка в регулярке
#'\.' - точка в регулярке

#r'\d{2}.*\d{2}.*\d{2}.*\d{2}.*\d{2}' - option



