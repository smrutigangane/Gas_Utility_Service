# service_requests/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Dashboard for support representatives
    path('status/', views.status_view, name='status'),  # Customer status view
    path('submit/', views.create_service_request, name='submit_request'),  # Create a new service request
  path('track/<int:request_id>/', views.track_request, name='track_request'),
    path('my-requests/', views.service_request_list, name='service_request_list'),  # Updated: Name changed to match redirect
    path('manage/', views.support_view, name='manage_requests'),  # Support representatives view for all requests
    path('manage/update/<int:request_id>/', views.update_request_status, name='update_request_status'),  # Update request status
]
