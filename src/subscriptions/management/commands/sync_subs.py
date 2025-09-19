from django.core.management.base import BaseCommand
from typing import Any 
from subscriptions.models import Subscription
class Command(BaseCommand):
    def handle(self, *args, **options):
        print("hello world")
        qs = Subscription.objects.all()
        for obj in qs:
            print(obj.groups.all())
            print(obj.permissons.all())
            
            # 6.0