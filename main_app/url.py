from django.urls import path

from main_app.views import index_main,send_index,get_index

urlpatterns = [
    path('', index_main),
    path('get_index', get_index, name="get_index"),
    path('send_index', send_index, name="send_index"),
]
