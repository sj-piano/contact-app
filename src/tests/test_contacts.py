import json

import pytest

from app.api import crud


def test_create_contact(test_app, monkeypatch):
    test_request_payload = {"name": "Bob Smith", "phone": "1234567890", "email": "bobsmith@foo.com"}
    test_response_payload = {"id": 1, "name": "Bob Smith", "phone": "1234567890", "email": "bobsmith@foo.com"}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    response = test_app.post("/contacts/", content=json.dumps(test_request_payload),)

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_create_contact_invalid_json(test_app):
    response = test_app.post("/contacts/", content=json.dumps({"name": "Bob Smith"}))
    assert response.status_code == 422


def test_read_contact(test_app, monkeypatch):
    test_data = {"id": 1, "name": "Bob Smith", "phone": "1234567890", "email": "bobsmith@foo.com"}

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/contacts/1")
    assert response.status_code == 200
    assert response.json() == test_data


def test_read_contact_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/contacts/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Contact not found"


def test_read_all_contacts(test_app, monkeypatch):
    test_data = [
        {"id": 1, "name": "Bob Smith", "phone": "1234567890", "email": "bobsmith@foo.com"},
        {"id": 2, "name": "Sarah Smith", "phone": "111222333", "email": "sarahsmith@foo.com"},
    ]

    async def mock_get_all():
        return test_data

    monkeypatch.setattr(crud, "get_all", mock_get_all)

    response = test_app.get("/contacts/")
    assert response.status_code == 200
    assert response.json() == test_data

