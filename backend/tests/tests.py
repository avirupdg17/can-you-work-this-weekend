import pytest
from flask import Flask, request, jsonify
import os
import sys
from inspect import getsourcefile

path_folders = os.environ['PATH'].split(':')
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(getsourcefile(lambda:0))))

if current_dir not in path_folders:
    sys.path.append(current_dir)

from flask_app.routes import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_get_personal_details(client):
    response = client.get('/get_personal_details')
    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "success"
    assert "data" in data
    assert "current_age" in data["data"]

def test_set_personal_details(client):
    data = {
        "current_age": "25",
        "fi_age": "28",
        "lifespan": "90"
    }
    
    response = client.post('/set_personal_details', data=data)
    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "success"

def test_get_market_expectations(client):
    response = client.get('/get_market_expectations')
    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "success"
    assert "data" in data
    assert "inflation" in data["data"]

def test_set_market_expectations(client):
    data = {
        "inflation": "7",
        "asset_classes": "[{'name': 'Savings Account', 'returns': 3, 'std': 0.25}, {'name': 'PPF', 'returns': 7, 'std': 0.5}, {'name': 'Mutual Funds', 'returns': 10, 'std': 10}]"
    }

    response = client.post('/set_market_expectations', data=data)
    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "success"
