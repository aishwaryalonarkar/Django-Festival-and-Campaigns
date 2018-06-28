# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import festmodel
from .models import campaign

class TableInline(admin.TabularInline):
	model = festmodel

class festInline(admin.ModelAdmin):
	fieldset=[
		(None,   {'fields':['festival_name']})
	]
	inlines=[TableInline]
	list_display = ('festival_name')
	list_filter = ['date']
	search_fields = ['month']

admin.site.register(festmodel)
admin.site.register(campaign)
# Register your models here.
