# mywebserver/notes/tests.py
from django.urls import reverse
from django.test import Client
import pytest

client = Client()


@pytest.mark.django_db
def test_home_url():
    response = client.get(reverse('home'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_week_notes_url():
    response = client.get(reverse('week_notes'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_week_note_url():
    response = client.get(reverse('create_week_note'))
    assert response.status_code == 200
