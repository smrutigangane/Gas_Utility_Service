from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from service_requests.models import CustomerProfile

class Command(BaseCommand):
    help = 'Create CustomerProfile for existing users'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            CustomerProfile.objects.get_or_create(user=user, account_number=user.username, address="")  # Fill in with relevant data if needed
        self.stdout.write(self.style.SUCCESS('Successfully created CustomerProfiles for all users'))
