from django.contrib import admin
from .models import Ticket
# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created")
    list_filter = ("status","created")
admin.site.register(Ticket, TicketAdmin)