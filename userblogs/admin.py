# from django.contrib import admin

# # Register your models here.
# from .models import Blog 
# admin.site.register(Blog)








from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blogtime', 'user', 'timestamp')

    def has_module_permission(self, request):
        """
        Allow only superusers and staff to see the Blog app.
        """
        return request.user.is_active and request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_staff

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
    