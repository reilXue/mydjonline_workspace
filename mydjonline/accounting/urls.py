from django.conf.urls import url
from accounting import views

urlpatterns = [
    url(r'^application',views.application,name='application'),
]
