from django.contrib import admin
from .models import Lead,Source,Campaign,Tag,LeadFollowUp,Requirement,Project,Booking,Closure,ProjectMatch
# Register your models here.

admin.site.register(Lead)
admin.site.register(Source)
admin.site.register(Campaign)
admin.site.register(Tag)
admin.site.register(LeadFollowUp)
admin.site.register(Requirement)
admin.site.register(Project)
admin.site.register(Booking)
admin.site.register(Closure)
admin.site.register(ProjectMatch)

