import pytest
from .models import Machine

# @pytest.mark.django_db
# def test_display_machine_detail_site(task, client):
#     pk = task.pk
#     response = client.get(f'/task-details/{pk}')
#     assert response.status_code == 200
#     assert 'name' in response.context
#     assert response.context['name'] == task.name


@pytest.mark.django_db
def test_add_machine(client):
    response = client.post('/add-machine/',
                           {'machine_model': 'Excavator',
                            'description': 'Machine for excavation',
                            'price': 5000})
    assert Machine.objects.get(machine_model='Excavator')
    assert response.status_code == 302



