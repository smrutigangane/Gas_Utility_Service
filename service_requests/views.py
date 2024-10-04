from django.shortcuts import render, redirect, get_object_or_404
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

@login_required
def create_service_request(request):
    """View to create a new service request."""
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customerprofile  # Associate with the logged-in user
            service_request.save()
            return redirect('service_request_list')  # Redirect to the list of service requests after submission
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/create_service_request.html', {'form': form})

@login_required
def service_request_list(request):
    """View to display a list of all service requests."""
    requests = ServiceRequest.objects.filter(customer=request.user.customerprofile)  # Fetch requests for the logged-in user
    return render(request, 'service_requests/service_request_list.html', {'requests': requests})

@login_required
def submit_request(request):
    """View to submit a new service request."""
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customerprofile  # Associate with the logged-in user
            service_request.save()
            return redirect('track_requests')  # Redirect to track_requests view after submission
    else:
        form = ServiceRequestForm()
    
    return render(request, 'service_requests/submit_request.html', {'form': form})

@login_required
def track_request(request, request_id):
    """View to track the status of a specific service request."""
    request_details = get_object_or_404(ServiceRequest, id=request_id, customer=request.user.customerprofile)
    return render(request, 'service_requests/track_request.html', {'request_details': request_details})

@login_required
def support_view(request):
    """View for managing service requests (removed permission checks)."""
    service_requests = ServiceRequest.objects.all()  # Retrieve all service requests for any logged-in user
    return render(request, 'service_requests/manage_requests.html', {'requests': service_requests})

@login_required
def update_request_status(request, request_id):
    """View to update the status of a service request."""
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        service_request.status = request.POST.get('status')  # Update status
        service_request.save()
        return redirect('manage_requests')
    return render(request, 'service_requests/update_request.html', {'service_request': service_request})

@login_required
def home_view(request):
    """View for the home page."""
    return render(request, 'home.html')

@login_required
def dashboard_view(request):
    """View for the dashboard to display all service requests."""
    service_requests = ServiceRequest.objects.all()  # Show all requests to any logged-in user
    return render(request, 'dashboard.html', {'service_requests': service_requests})

@login_required
def status_view(request):
    """View to display service request status."""
    service_requests = ServiceRequest.objects.filter(customer=request.user.customerprofile)
    logger.info(f"Customer: {request.user.customerprofile}, Requests: {service_requests}")
    if not service_requests:
        return HttpResponse("No service requests found for this customer.")
    return render(request, 'service_requests/status.html', {'service_requests': service_requests})
