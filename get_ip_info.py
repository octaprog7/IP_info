#!/usr/bin/env python3
import requests
import http.client
# see http://geolocation-db.com/


def get_ip_info(ip: str = "", position: bool = True) -> dict:
    """
    Возвращает информацию по IP адресу (ip). Если ip=="", то возвращает IP этого ПК.
    param ip: IP-адрес
    param position:
    return: словарь с информацией. Ключи: country_code, country_name, city, postal, latitude, longitude, IPv4, state
    """
    if not ip:
        ip = get_my_white_ip()
    _url = "https://geolocation-db.com/json/"
    s = f"{_url}{ip}&position={position}"
    with requests.get(s, stream=True) as req:
        return req.json()


def get_my_white_ip() -> str:
    """Возвращает белый внешний IP-адрес ПК, выполняющего эту функцию."""
    # res = ""
    conn = None
    try:
        conn = http.client.HTTPConnection("ifconfig.me")
        conn.request("GET", "/ip")
        res = conn.getresponse().read()
    finally:
        conn.close()
    return res.decode('utf-8')


if __name__ == "__main__":
    my_ip: str = get_my_white_ip()
    print(f"my white IP: {my_ip}")
    print(f"{my_ip} info:")
    #
    r = get_ip_info(my_ip)
    for k, v in r.items():
        print(f"{k}:\t{v}")