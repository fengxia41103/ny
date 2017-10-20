from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver

from lxca.models import *
from lxca.catalog_models import *
from lxca.architect_models import *
from lxca.order_models import *


@receiver(post_save, sender=OrderSolution)
def OrderSolution_post_save(sender, instance, **kwargs):
    if instance.solution and instance.status == 1:
        """Auto create Order-hw for each hardware
        defined in the reference architecture.
        """
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

    elif instance.status == 2 and not MfgSolution.objects.filter(order=instance):
        """Auto generage MfgSolution and its children endpoints
        when moving OrderSolution's status from `draft` to `mfg`.
        """
        mfg = MfgSolution(order=instance)
        mfg.save()
        for r in instance.racks:
            for i in range(r.qty):
                tmp = MfgRack(solution=mfg, order=r)
                tmp.save()
        for r in instance.pdus:
            for i in range(r.qty):
                tmp = MfgPdu(solution=mfg, order=r)
                tmp.save()
        for r in instance.switches:
            for i in range(r.qty):
                tmp = MfgSwitch(solution=mfg, order=r)
                tmp.save()
        for r in instance.servers:
            for i in range(r.qty):
                tmp = MfgServer(solution=mfg, order=r)
                tmp.save()
