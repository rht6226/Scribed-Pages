from django.urls import path, include
from .views import home, create_notebook

urlpatterns = [
      path('', home, name='home'),
      path('notebook/create', create_notebook, name='create_notebook')
]