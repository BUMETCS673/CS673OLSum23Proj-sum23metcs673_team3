import requests
import os
import json

BASE_URL = "http://127.0.0.1:8000/"
CSRF_TOKEN = os.getenv("CSRF_TOKEN")
SESSION_ID=os.getenv("SESSION_ID")
"DcVMemjSJtbgTqkK0dbXApqT8lshA8zz"


# def test_auth_users_good():
#     url = "http://127.0.0.1:8000/login/api-auth/"
#     data= {
#         "username":"corydon-test",
#         "password": "pass"
#     }
#     response = requests.post(url,data=data)
#     print(response)
#     assert response.status_code == 200
#     assert response.headers["content-type"]== "text/html; charset=utf-8"
#
# def test_auth_users_bad():
#     url = "http://127.0.0.1:8000/login/api-auth/"
#     data= {
#         "username":"corydon-test",
#         "password": "pa"
#     }
#     response = requests.post(url,data=data)
#     print(response)
#     assert response.status_code == 403


def test_set_filter():
    url = BASE_URL + "foods/set-filter"
    headers = {
        "X-CSRFToken": CSRF_TOKEN,
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "filter": "week"
    })
    response = requests.post(url, data=data, headers=headers)
    print(response)
    assert response.status_code == 200


def test_get_foods_api():
    url = BASE_URL + "foods/get-food-names"
    headers = {
        "X-CSRFToken": CSRF_TOKEN,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    response_json = response.json()
    assert len(response_json["food_name"]) > 0
    assert response_json["food_name"][0] == "pear"
    assert response.status_code == 200


def test_create_log_entry():
    url = "http://127.0.0.1:8000/foods/create-log-entry"
    headers = {
        "X-CSRFToken": CSRF_TOKEN,
        "Content-Type": "application/json",
        "Cookie": f"csrftoken={CSRF_TOKEN}; sessionid={SESSION_ID}"
    }
    data = json.dumps({
        "food_item_name": "apple",
        "num_servings": "4"
    })
    response = requests.post(url, data=data, headers=headers)
    print(response)
    assert response.status_code == 200


def test_create_food_item():
    url = BASE_URL + "foods/create-food-item"
    headers = {
        "X-CSRFToken": CSRF_TOKEN,
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "food_item_name": "goldfish",
        "calories": "120"
    })
    response = requests.post(url, data=data, headers=headers)
    print(response)
    assert response.status_code == 200


