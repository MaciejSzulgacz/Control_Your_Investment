"""ControlYourInvestment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from MainApp import views as ex_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ex_views.BaseView.as_view(), name="base"),
    path('add-task/', ex_views.TaskCreateView.as_view(), name="add-task"),
    path('delete-task/<int:my_id>/', ex_views.TaskDeleteView.as_view(), name="delete-task"),
    path('edit-task/<pk>', ex_views.TaskUpdateView.as_view(), name="edit-task"),
    path('add-machine/', ex_views.MachineCreateView.as_view(), name="add-machine"),
    path('delete-machine/<int:my_id>/', ex_views.MachineDeleteView.as_view(), name="delete-machine"),
    path('edit-machine/<pk>', ex_views.MachineUpdateView.as_view(), name="edit-machine"),
    path('add-person/', ex_views.PersonCreateView.as_view(), name="add-person"),
    path('delete-person/<int:my_id>/', ex_views.PersonDeleteView.as_view(), name="delete-person"),
    path('edit-person/<pk>', ex_views.PersonUpdateView.as_view(), name="edit-person"),
    path('login/', ex_views.LoginView.as_view(), name="login"),
    path('logout/', ex_views.LogoutView.as_view(), name="logout"),
    path('add-image/', ex_views.ImageCreateView.as_view(), name="add-image"),
    path('task-details/<int:my_id>/', ex_views.DetailsTaskView.as_view(), name="details-task"),
    path('person-list', ex_views.PersonListView.as_view(), name="person-list"),
    path('machine-list', ex_views.MachineListView.as_view(), name="machine-list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
