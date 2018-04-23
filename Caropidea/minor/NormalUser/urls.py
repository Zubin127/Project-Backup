from django.conf.urls import url
from NormalUser import views

app_name = 'NormalUser'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    #Normal User Registration
    #url(r'^register_Normal/',views.registerNormal, name='registerNormal'),

]
