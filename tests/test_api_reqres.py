import requests
import pytest


@pytest.mark.skipif(reason="falta api key")
def test_get_users(base_url, header_request):
    response = requests.get(f"{base_url}/2", headers=header_request)
    assert response.status_code == 200
    body = response.json()
    assert "data" in body
    assert body["data"]["id"] == 2

@pytest.mark.skipif(reason="falta api key")
def test_create_user(base_url, header_request):
    payload = {"name": "Maxi", "job": "Software Developer"}
    response = requests.post(base_url, headers=header_request, json=payload)
    assert response.status_code == 201
    body = response.json()
    assert body["name"] == payload["name"]

@pytest.mark.skipif(reason="falta api key")
def test_delete_user(base_url, header_request):
    response = requests.delete(f"{base_url}/2", headers=header_request)
    assert response.status_code == 204
