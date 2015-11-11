from django.contrib import admin
from coopInfo.models import Cooperative , Person , State

class PersonAdmin(admin.ModelAdmin):
	list_display = ('name', 'sex','ethnicity', 'coopId','title')
	search_fields = ['name']
	list_filter = ['ethnicity', 'title', 'sex']

class PersonInline(admin.TabularInline):
    model = Person
    extra = 8

class CooperativeAdmin(admin.ModelAdmin):
	list_display = ('name', 'stateId','website' )
	search_fields = ['name']
	list_filter = ['stateId']
	inlines = [PersonInline]
	fieldsets = [
	    ('Basic info', {'fields': ['name', 'website', 'acronym']}),
	    ('Mail Info', {'fields': ['streetAddress', 'mailAddress']}),
	    ('Contact', {'fields': ['email', 'phone']}),
	    ('Administrative', {'fields':['servingTime','nextElectionTerms','annualMeeting','montlyMeeting']}),
	    ('Misc', {'fields': ['consumers','numberOfEmployees','milesOfLines','countiesServed']}),
	    ('Documents', {'fields': ['bylaws', 'is990present']})
	    ]

#Customise Admin site 
admin.site.site_header = 'Electric Coop Backoffice'
admin.site.site_title = 'Electric Coop Backoffice'

# Register your models here.
admin.site.register(Cooperative, CooperativeAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(State)