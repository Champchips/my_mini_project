from django.urls import path
from . import views as v

urlpatterns = [
    path('create/', v.poll_create, name='poll_create'),
    path('detail/', v.poll_detail, name='poll_detail'),
    path('update/', v.poll_update, name='poll_update'),
    path('view/', v.poll_views, name='poll_views')
]
