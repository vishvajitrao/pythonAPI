from django.urls import path

from myapp.views import PersonList, PersonDetails, PersonUpdate, PersonDelete, \
    CreateUser, MyappList,MyappDetail
from . import views
#from views import PersonList, PersonDetails, PersonUpdate
urlpatterns = [
    path('myapp', views.firstProject, name='firstProject'),
    path('users', PersonList.as_view(), name=''),
    path('users/<int:pk>', PersonDetails.as_view(), name='PersonDetails'),
    path('update/<int:pk>', PersonUpdate.as_view(), name='PersonUpdate'),
    path('delete/<int:pk>', PersonDelete.as_view(), name='PersonDelete'),
    path('createuser', CreateUser.as_view(), name='CreateUser'),
    path('myapps', MyappList.as_view(), name='MyappList'),
    path('myapps/<int:pk>', MyappDetail.as_view(), name='MyappDetail'),


    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('status/', views.status, name='status'),

    path('registration/', views.customRegistration, name='customRegistration'),

]


