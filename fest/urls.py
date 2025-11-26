from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('bulk/registration/', views.bulk_registration, name='bulk_registration'),
    path('calling/list/', views.calling_list, name='calling_list'),
    path('get-events/', views.get_events, name='get_events'),
     path('calling/list/generate/', views.generate_calling_list, name='generate_calling_list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
