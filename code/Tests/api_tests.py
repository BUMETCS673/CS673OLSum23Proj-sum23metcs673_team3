import requests
import os
import json

BASE_URL = "http://localhost:8000/"
CSRF_TOKEN = os.getenv("CSRF_TOKEN")
SESSION_ID=os.getenv("SESSION_ID")

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
    url = BASE_URL+"foods/create-log-entry"
    headers = {
        "X-CSRFToken":{CSRF_TOKEN},
        "Content-Type": "application/json",
        "Cookie": f"csrftoken={CSRF_TOKEN}; sessionid={SESSION_ID}"
    }
    data = json.dumps({
        "food_item_name": "apple",
        "num_servings": "4",
        "dateHad": "2023-06-17T03:15"
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

def test_delete_log_entry():
    url = BASE_URL + "foods/delete-log-entry"
    headers = {
        "X-CSRFToken": CSRF_TOKEN
    }
    data = {
        "log_item_selected":"29"
    }
    response = requests.post(url, data=data, headers=headers)
    print(response)
    assert response.status_code == 200

def test_cal_per_day():
    url = BASE_URL + "foods/cal-per-day"
    headers = {
        "X-CSRFToken": CSRF_TOKEN
    }
    response = requests.post(url, headers=headers)
    print(response)
    response_json = response.json()
    assert response.status_code == 200
    assert "calories" in response_json

def test_cal_per_day():
    url = BASE_URL + "foods/fav-food"
    headers = {
        "X-CSRFToken": CSRF_TOKEN
    }
    response = requests.post(url, headers=headers)
    print(response)
    response_json = response.json()
    assert response.status_code == 200
    assert "labels" in response_json
    assert "numbers" in response_json