from django.apps import AppConfig

class SalesConfig(AppConfig):
    name = 'sales'

    def ready(self):
        print("-------ready----------")
        import sales.signals
        # post_save.connect(create_db_user, sender=Salesperson)