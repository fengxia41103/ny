from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver

from lxca.models import *
from lxca.catalog_models import *
from lxca.architect_models import *
from lxca.order_models import *


@receiver(post_save, sender=OrderSolution)
def OrderSolution_post_save(sender, instance, **kwargs):
    """Auto create Order-hw for each hardware
    defined in the reference architecture.
    """
    if instance.solution and instance.status == 1:
        for r in instance.solution.applications.all():
            OrderApplication(order=instance, template=r).save()
        for r in instance.solution.racks.all():
            OrderRack(order=instance, template=r).save()
        for r in instance.solution.powers.all():
            OrderPdu(order=instance, template=r).save()
        for r in instance.solution.switches.all():
            OrderSwitch(order=instance, template=r).save()
        for r in instance.solution.servers.all():
            OrderServer(order=instance, template=r).save()
