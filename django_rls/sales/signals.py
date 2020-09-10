from .models import Salesperson
from django.db.models.signals import post_save
from django.db import connection
from django.dispatch import receiver


@receiver(post_save, sender=Salesperson)
def create_db_user(sender, instance, created, **kwargs):
    print("---post---save")
    if created:
        user_id = instance.id
        print("------createrd--------",user_id)
        with connection.cursor() as cursor:
            # cursor.execute(f'CREATE ROLE "{user_id}"')
            # cursor.execute(f'GRANT sales_client TO "{user_id}"')
            # cursor.execute(f'GRANT select ON sales_client TO "{user_id}"')
            # cursor.execute(f'GRANT auth_user TO "{user_id}"')

            cursor.execute(
                f'CREATE POLICY salesperson_clients_28 ON sales_client USING (Salesperson_id::integer = 28)')

            cursor.execute(f'ALTER TABLE sales_client ENABLE ROW LEVEL SECURITY')

# post_save.connect(create_db_user, sender=Salesperson)

# Password@321

# $Dd$89800
