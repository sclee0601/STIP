from django.contrib import admin

# Register your models here.

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Bill, Session
# Register your models here.

admin.site.register(Session)

@admin.register(Bill)
class BillAdmin(ImportExportModelAdmin):
    pass


