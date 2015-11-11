from django.contrib import admin

from .models import State, County

class CountyAdmin(admin.ModelAdmin):
	#list_display = ('name', 'state')
	search_fields = ['name']
	#list_filter = ['state']


admin.site.register(State)
admin.site.register(County, CountyAdmin)