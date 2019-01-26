from django.urls import path
from .views import login_user, logout_user, signup, dashboard, edit_profile
from django.conf.urls.static import static
from scribe import settings


urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path(r'login', login_user, name='login'),
    path(r'logout', logout_user, name='logout'),
    path(r'signup', signup, name='signup'),
    path(r'dashboard', dashboard, name='dashboard'),
    path(r'edit_profile', edit_profile, name='edit_profile')
]

