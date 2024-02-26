from django.urls import path
from .views import HomePage, AdminPageView, restricted_page

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('admin/', AdminPageView.as_view(), name='admin_page'),
    path('restricted/', restricted_page, name='restricted_page')
]