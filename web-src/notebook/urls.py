from django.urls import path, include
from .views import home, create_notebook, view_notebook, getlist, getAudio, edit_notebook, edit_article,search, gettags,html_to_pdf_view

urlpatterns = [
      path('', home, name='home'),
      path('notebook/create', create_notebook, name='create_notebook'),
      path('notebook/view/<slug:uid>', view_notebook, name='view_notebook'),
      path('notebook/edit/<slug:uid>', edit_notebook, name='edit_notebook'),
      path('notebook/edit/article/<slug:uid>', edit_article, name='edit_article'),
      path('getList/<slug:uid>', getlist, name='getList'),
      path('getAudio', getAudio, name='getAudio'),
      path('notebook/pdf/<slug:uid>', html_to_pdf_view, name='pdf'),
      path('search/<slug:uid>', search, name='search'),
      path('getTags',gettags,name='gettags'),
]
