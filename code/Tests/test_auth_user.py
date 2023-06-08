import requests
def test_auth_users_good():
    url = "http://127.0.0.1:8000/login/api-auth/"
    data= {
        "username":"corydon-test",
        "password": "pass"
    }
    response = requests.post(url,data=data)
    print(response)
    assert response.status_code == 200
    assert response.headers["content-type"]== "text/html; charset=utf-8"

def test_auth_users_bad():
    url = "http://127.0.0.1:8000/login/api-auth/"
    data= {
        "username":"corydon-test",
        "password": "pa"
    }
    response = requests.post(url,data=data)
    print(response)
    assert response.status_code == 403