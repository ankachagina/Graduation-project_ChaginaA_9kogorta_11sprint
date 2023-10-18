import configuration
import requests
import data


# Создание нового заказа
def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_AN_ORDER,  # подставляем полный url
                         json=body,
                         headers=data.headers)  # а здесь заголовки


def get_orders_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_AN_ORDER_BY_TRACK,
                         params=track)
