import pytest
from django.test import Client
from MainApp.models import Machine, Person


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def machine():
    return Machine.objects.create(
        machine_model='fake machine',
        description='fake machine description',)


@pytest.fixture
def person():
    return Person.objects.create(
        full_name='fake person',
        position='fake position',)
