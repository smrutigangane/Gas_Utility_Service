# service_requests/tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import ServiceRequest, CustomerProfile

class ServiceRequestTestCase(TestCase):
    def setUp(self):
        # Create a test user and customer profile
        self.user = User.objects.create(username='testuser', password='password')
        self.customer = CustomerProfile.objects.create(user=self.user, account_number='12345', address='Test Address')

    def test_create_service_request(self):
        # Create a service request and test its creation
        request = ServiceRequest.objects.create(
            customer=self.customer,
            service_type='Gas Leak',
            description='Suspected gas leak at home'
        )
        self.assertEqual(request.status, 'Pending')  # New service requests should be 'Pending'
        self.assertEqual(request.customer, self.customer)
