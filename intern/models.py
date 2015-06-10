# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from django.forms import ModelForm
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.generic import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from annoying.fields import JSONField # django-annoying
from django.db.models import Q
from datetime import datetime as dt
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from localflavor.us.forms import USPhoneNumberField


class MyBaseModel (models.Model):
	# fields
	hash = models.CharField (
		max_length = 256, # we don't expect using a hash more than 256-bit long!
		null = True,
		blank = True,
		default = '',
		verbose_name = u'MD5 hash'
	)
		
	# basic value fields
	name = models.CharField(
			default = None,
			max_length = 128,
			verbose_name = u'名称'
		)
	description = models.TextField (
			null=True, 
			blank=True,
			verbose_name = u'描述'
		)
	
	# help text
	help_text = models.CharField (
			max_length = 64,
			null = True,
			blank = True,
			verbose_name = u'帮助提示'
		)

	# attachments
	attachments = GenericRelation('Attachment')
	
	# this is an Abstract model
	class Meta:
		abstract=True

	def __unicode__(self):
		return self.name

######################################################
#
#	Tags
#
#####################################################
class MyTaggedItem (models.Model):
	# basic value fields
	tag = models.SlugField(
			default = '',
			max_length = 16,
			verbose_name = u'Tag'
	)	
	def __unicode__(self):
		return self.tag

######################################################
#
#	Attachments
#
#####################################################
class Attachment (models.Model):
	# generic foreign key to base model
	# so we can link attachment to any model defined below
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	# instance fields
	created_by = models.ForeignKey (
		User,
		blank = True,
		null = True,
		default = None,
		verbose_name = u'创建用户',
		help_text = ''
	)
		
	# basic value fields
	name = models.CharField(
		default = 'default name',
		max_length = 64,
		verbose_name = u'附件名称'
	)
	description = models.CharField (
		max_length = 64,
		default = 'default description',
		verbose_name = u'附件描述'
	)
	file = models.FileField (
		upload_to = '%Y/%m/%d',
		verbose_name = u'附件',
		help_text = u'附件'
	)	

	def __unicode__(self):
		return self.file.name

class AttachmentForm(ModelForm):
	class Meta:
		model = Attachment
		fields = ['description','file']

######################################################
#
#	App specific models
#
#####################################################
class MyExternalContact(MyBaseModel):
	email = models.EmailField()
	phone = USPhoneNumberField()

	def __unicode__(self):
		return self.name

class MyStatus(models.Model):
	STATUS_CHOICES = (
		(1,u'initialized'),
		(2,u'dept submitted'),
		(3,u'college submitted'),
		(4,u'approved'),
	)														
	status = models.IntegerField(
		default = 1,
		choices = STATUS_CHOICES
	)
	contact = models.ForeignKey(
		'MyExternalContact',
		verbose_name = u'Conact in charge'
	)
	def __unicode__(self):
		return self.get_status_display()

class MyStatusAudit(models.Model):
	application = models.ForeignKey(
		'MyApplication',
		verbose_name = u'Application'
	)
	old_status = models.CharField(
		max_length = 64,
		default = '',
		verbose_name = u'Old status'
	)
	new_status = models.CharField(
		max_length = 64,
		default = '',
		verbose_name = u'New status'
	)	
	contact = models.ForeignKey(
		'MyExternalContact',
		verbose_name = u'Contact person'
	)
	created = models.DateTimeField(
		auto_now_add=True,
	)
	comment = models.TextField(
		null = True,
		blank = True,
		verbose_name = u'Status change comment'
	)		

class MyApplication(models.Model):
	created = models.DateTimeField(
		auto_now_add=True,
	)	
	application_id = models.CharField(
		max_length = 64,
		null = True,
		blank = True,
		verbose_name = u'Application ID'
	)
	applicant_name = models.CharField(
		max_length = 256,
		verbose_name = u'Applicant name'
	)
	start_date = models.DateField(
		verbose_name = u'Starting date'
	)
	end_date = models.DateField(
		verbose_name = u'End date'
	)
	status = models.ForeignKey(
		'MyStatus',
		verbose_name = u'Application status'
	)
	def _duration_in_days(self):
		return (self.end_date-self.start_date).days
	duration_in_days = property(_duration_in_days)	
	
	def _lead_in_days(self):
		return (self.start_date-self.created.date()).days
	lead_in_days = property(_lead_in_days)

	def _time_to_start_in_days(self):
		return (self.start_date-dt.now().date()).days
	time_to_start_in_days = property(_time_to_start_in_days)

	def __unicode__(self):
		return '%s (%s)'%(self.applicant_name,self.application_id)

@receiver(pre_save,sender=MyApplication)
def application_status_change_handler(sender, **kwargs):
	instance = kwargs.get('instance')
	if instance.id: 
		original = MyApplication.objects.get(id=instance.id)
		if original.status != instance.status:
			old_status = original.status.__unicode__()
			new_status = instance.status.__unicode__()
			# create an audit trail
			audit = MyStatusAudit(
				application = instance,		
				old_status = old_status,
				new_status = new_status,
				contact = original.status.contact,
				comment = u'Status changed'				
			)
			audit.save()

			# send an alert
			# TODO: move this to background through redis queue
			send_mail(
				subject = '%s status change'%instance.application_id, 
				message = '%s -> %s'%(old_status,new_status), 
				from_email = 'fengxia41103@gmail.com',
				recipient_list = [original.status.contact.email], 
				fail_silently=False)