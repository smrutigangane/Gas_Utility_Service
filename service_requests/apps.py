from django.apps import AppConfig


class ServiceRequestsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'service_requests'

    def ready(self):
        import service_requests.signals  # Adjust the import based on your app structure
