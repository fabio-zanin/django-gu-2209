from django.conf.urls import handler404, handler500
from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('produto/<int:pk>', views.produto, name='produto'),
    path('contatos/', views.contato, name='contatos'),
]


handler404 = views.error404
handler500 = views.error500
