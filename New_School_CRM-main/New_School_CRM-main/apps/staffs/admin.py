from django.contrib import admin
from .models import Staff, LeaveRequeststaff

class StaffAdmin(admin.ModelAdmin):
    list_display = ('surname', 'firstname', 'other_name', 'gender', 'date_of_birth', 'date_of_admission', 'mobile_number', 'current_status')
    search_fields = ('surname', 'firstname', 'other_name', 'mobile_number')
    list_filter = ('gender', 'current_status')
    ordering = ('surname', 'firstname', 'other_name')
    readonly_fields = ('date_of_admission',)




class LeaveRequeststaffAdmin(admin.ModelAdmin):
    list_display =('staff', 'reason','date_applied','status')
    
    
admin.site.register(Staff, StaffAdmin)
admin.site.register(LeaveRequeststaff, LeaveRequeststaffAdmin)