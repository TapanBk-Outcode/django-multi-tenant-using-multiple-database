from django.contrib import admin
from .models import Office


class AdminOffice(admin.ModelAdmin):
	list_display = ["id", "name", "address"]


admin.site.register(Office, AdminOffice)
