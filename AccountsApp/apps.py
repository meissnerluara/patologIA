from django.apps import AppConfig


class AccountsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AccountsApp'

    # def ready(self):
    #     from AccountsApp.signals import create_groups_and_permissions
    #     from django.db.models.signals import post_migrate
    #     post_migrate.connect(create_groups_and_permissions)