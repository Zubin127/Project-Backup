from django.conf.urls import url
from BusinessUser import views

app_name = 'BusinessUser'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #Business User registration

]
