# myapp/api.py
from django.http import HttpResponse
from tastypie import resources, fields, utils
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from lxca.models import *

# tastypie API urls
from tastypie.api import Api
v1_api = Api(api_name='v1')


def build_content_type(format, encoding="utf-8"):
    """
    Appends character encoding to the provided format if not already present.
    """
    if "charset" in format:
        return format

    return "%s; charset=%s" % (format, encoding)


class MyModelResource(resources.ModelResource):

    def create_response(self, request, data, response_class=HttpResponse, **response_kwargs):
        """
        Extracts the common "which-format/serialize/return-response" cycle.

        Mostly a useful shortcut/hook.
        """
        desired_format = self.determine_format(request)
        serialized = self.serialize(request, data, desired_format)
        return response_class(content=serialized,
                              content_type=build_content_type(desired_format),
                              **response_kwargs)


######################################################
#
#	Catalog resources
#
#####################################################
class CatalogRackResource(MyModelResource):

    class Meta:
        queryset = CatalogRack.objects.all()
        resource_name = "racks"


class CatalogPduResource(MyModelResource):

    class Meta:
        queryset = CatalogPdu.objects.all()
        resource_name = "pdus"


class CatalogSwitchResource(MyModelResource):

    class Meta:
        queryset = CatalogSwitch.objects.all()
        resource_name = "switches"


class CatalogServerResource(MyModelResource):

    class Meta:
        queryset = CatalogServer.objects.all()
        resource_name = "servers"


######################################################
#
#	SA resources
#
#####################################################
class ArchitectLxcaResource(MyModelResource):

    class Meta:
        queryset = ArchitectLxca.objects.all()
        resource_name = "lxca"


class ArchitectComplianceResource(MyModelResource):

    class Meta:
        queryset = ArchitectCompliance.objects.all()
        resource_name = "compliance"


class ArchitectFirmwareResource(MyModelResource):

    class Meta:
        queryset = ArchitectFirmwareRepo.objects.all()
        resource_name = "firmware"


class ArchitectSolutionResource(MyModelResource):
    lxca = fields.ForeignKey(ArchitectLxcaResource,
                             "lxca", full=True)
    compliance = fields.ForeignKey(ArchitectComplianceResource,
                                   "compliance", full=True)
    firmware_repo = fields.ForeignKey(ArchitectFirmwareResource,
                                      "firmware",
                                      full=True,
                                      null=True)

    class Meta:
        queryset = ArchitectSolution.objects.all()
        resource_name = "solutions"

# Register resources
v1_api.register(CatalogRackResource())
v1_api.register(CatalogPduResource())
v1_api.register(CatalogSwitchResource())
v1_api.register(CatalogServerResource())
v1_api.register(ArchitectLxcaResource())
v1_api.register(ArchitectFirmwareResource())
v1_api.register(ArchitectComplianceResource())
v1_api.register(ArchitectSolutionResource())
