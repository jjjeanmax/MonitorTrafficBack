from django.contrib import admin
from .models import Monitor


@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    list_display = ["continent",
                    "country",
                    "city",
                    "capital",
                    "datetime",
                    "ip",
                    ]
