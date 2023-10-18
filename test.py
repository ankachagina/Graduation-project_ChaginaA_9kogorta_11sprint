import data
import senden_stand_request

def get_trek_order():
    # Копируется словарь с телом запроса из файла data
    order_body = data.order_body.copy()
    order_body["firstName"] = 'Vasilisa'
    responce = senden_stand_request.create_new_order(order_body)
    # Запоминаем трек заказа
    return str(responce.json()["track"])


def positive_assert():
    number_track = get_trek_order()
    current_param = data.get_param.copy()
    current_param['t'] = number_track
    # в переменную response сохраняется результат запроса на создание набора под авторизованным пользователем
    response = senden_stand_request.get_orders_by_track(current_param)
    # Проверить код ответа
    assert response.status_code == 200


def test_create_order_and_get_order_by_numer_track():
    positive_assert()
