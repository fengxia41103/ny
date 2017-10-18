from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver

from lxca.models import *

###################################################
#
#	MyOrder signals
#
###################################################


@receiver(post_save, sender=OrderSolution)
def OrderSolution_post_save(sender, instance, **kwargs):
    """Auto create order line items based on the solution
    one has picked.

    These line items will then be used for configuring this order.
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
