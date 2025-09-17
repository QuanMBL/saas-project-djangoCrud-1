from django.db import models
from django.contrib.auth.models import Group, Permission

SUBSCRIPTION_PERMISSIONS = [
    ("basic", "Basic Perm"),
    ("pro", "Pro Perm"),
    ("advanced", "Advanced Perm"),
    ("basic_ai", "Basic AI Perm"),
]


# Create your models here.
class Subscription(models.Model):
    name = models.CharField(max_length=120)
    groups = models.ManyToManyField(Group, blank=True)
    permissons = models.ManyToManyField(
        Permission,
        limit_choices_to={
            "content_type__app_label": "subscriptions",
            "codename__in": [x[0] for x in SUBSCRIPTION_PERMISSIONS ]
        },
    )

    class Meta:
        permissions = SUBSCRIPTION_PERMISSIONS
