#Марк Чукарин 6я когорта-Финальный проект. Инженер по тестированию плюс
import data
import configuration
import requests


def post_create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


def get_new_order_track():
    order_response = post_create_order(data.order_body)
    order_track = order_response.json()["track"]
    return order_track


def get_order(order_track):
    order_track_url = configuration.ORDER_TRACK_PATH + "?t=" + str(order_track)
    return requests.get(configuration.URL_SERVICE + order_track_url, headers=data.headers)


def test_get_order():
    track = get_new_order_track()
    order_response = get_order(track)
    assert order_response.status_code == 200
    assert order_response.json()