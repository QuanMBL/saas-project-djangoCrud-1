from django.db import models
from django.contrib.auth.models import Group, Permission
from django.conf import settings

from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL
AlLLOW_CUSTOM_GROUPS= True
SUBSCRIPTION_PERMISSIONS = [
    ("basic", "Basic Perm"),
    ("pro", "Pro Perm"),
    ("advanced", "Advanced Perm"),
    ("basic_ai", "Basic AI Perm"),
]


# Create your models here.
class Subscription(models.Model):
    name = models.CharField(max_length=120)
    active = models.BooleanField(default=True)   
    groups = models.ManyToManyField(Group, blank=True)
    
    permissons = models.ManyToManyField(
        Permission,
        limit_choices_to={
            "content_type__app_label": "subscriptions",
            "codename__in": [x[0] for x in SUBSCRIPTION_PERMISSIONS ]
        },
    )
    def __str__(self):
        return f"{self.name}"

    class Meta:
        permissions = SUBSCRIPTION_PERMISSIONS

class UserSubscription(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription,on_delete=models.SET_NULL,null=True,blank=True)
    active = models.BooleanField(default=True)
    
    
def user_sub_post_save(sender, instance, *args, **kwargs):
    user_sub_instance = instance   
    user = user_sub_instance.user 
    subscription_obj = user_sub_instance.subscription
    groups_ids = []
    if subscription_obj is not None:
        groups = subscription_obj.groups.all()
        groups_ids = groups.value_list('id', flat = True)
    
    if not AlLLOW_CUSTOM_GROUPS:
        user.group.set(groups_ids)
    else:
        subs_qs = Subscription.objects.filter(active= True)
        if subscription_obj is not None:
            subs_qs = subs_qs.exclude(id=subscription_obj.id)
        subs_groups = subs_qs.values_list("groups__ids",flat=True)
        subs_groups_set = set(subs_groups)
        # groups_ids = groups.value_list('id', flat = True)
        current_groups = user.groups.all().value_list('id', flat = True)
        groups_ids_set = set(groups_ids)
        current_groups_set = set(current_groups) - subs_groups_set
        final_groups_ids = list(groups_ids_set|current_groups_set)
        user.group.set(final_groups_ids)
    
#Đây là phần save của database  
post_save.connect(user_sub_post_save,sender=UserSubscription)

