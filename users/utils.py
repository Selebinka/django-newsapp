from oauth2_provider.models import Application


def get_client_id_and_client_secret(name: str):
    application = Application.objects.filter(name=name).first()
    if not application:
        return None
    return application.client_id, application.client_secret

