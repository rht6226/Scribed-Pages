from django.urls import path
from .views import home, create_notebook, view_notebook

urlpatterns = [
      path(r'', home, name='home'),
      path(r'notebook/create', create_notebook, name='create_notebook'),
      path(r'notebook/view/<slug:uid>', view_notebook, name='view_notebook'),
]