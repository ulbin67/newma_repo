from django.contrib import admin
from .models import apply,get_num

# Register your models here.
# admin.site.register(apply)
admin.site.register(get_num)

@admin.register(apply)
class ApplyAdmin(admin.ModelAdmin):
    field_names = tuple([f.name for f in apply._meta.get_fields()])
    list_display = field_names
    list_filter = ('apply_at',)
