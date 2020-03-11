from django.urls import path
from . import views as v

urlpatterns = [
    path('create/', v.poll_create, name='poll_create'),
    path('vote/<int:poll_id>/<int:choice_id>', v.vote_poll, name='vote_poll'),
    path('vote/<int:poll_id>', v.poll_vote, name='poll_vote'),
    path('detail/', v.poll_detail, name='poll_detail'),
    path('my_poll/', v.my_poll, name='my_poll'),
    path('update/<int:poll_id>/choice/add', v.add_choice, name='add_choice'),
    path('choice/<int:choice_id>/delete', v.delete_choice, name='delete_choice'),
    path('update/poll/<int:poll_id>', v.poll_update, name='poll_update'),
    path('update/<int:poll_id>', v.poll_choice_update, name='poll_choice_update'),
    path('view/<int:poll_id>/', v.poll_views, name='poll_views')
]
