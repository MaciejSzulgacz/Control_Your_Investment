import pytest
from .models import Machine, Person


@pytest.mark.django_db
def test_add_machine(client):
    response = client.post('/add-machine/',
                           {'machine_model': 'Excavator',
                            'description': 'Machine for excavation'})
    assert Machine.objects.get(machine_model='Excavator')
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_person(client):
    response = client.post('/add-person/',
                           {'full_name': 'Michał Lewandowski',
                            'position': 'Construction Manager'})
    assert Person.objects.get(full_name='Michał Lewandowski')
    assert response.status_code == 302


@pytest.mark.django_db
def test_edit_machine(client, machine):
    response = client.post(f'/edit-machine/{machine.pk}',
                           {'machine_model': 'Excavator',
                            'description': 'Machine for excavation'})
    assert Machine.objects.get(machine_model='Excavator')
    assert response.status_code == 302


@pytest.mark.django_db
def test_edit_person(client, person):
    response = client.post(f'/edit-person/{person.pk}',
                           {'full_name': 'Michał Nowak',
                            'position': 'Side Manager'})
    assert Person.objects.get(full_name='Michał Nowak')
    assert response.status_code == 302


@pytest.mark.django_db
def test_delete_machine(client, machine):
    response = client.post(f'/delete-machine/{machine.pk}', )
    assert Machine.objects.get(machine_model=machine.machine_model)
    assert response.status_code == 301


@pytest.mark.django_db
def test_delete_person(client, person):
    response = client.post(f'/delete-person/{person.pk}',)
    assert Person.objects.get(full_name=person.full_name)
    assert response.status_code == 301
