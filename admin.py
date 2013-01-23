from django.contrib import admin
from frontpage.models import Project, Update

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = [
        (None,           {'fields': ['title', 'description']}),
        ('URLs',         {'fields': ['url','github','slug']}),
        ('Full text',    {'fields': ['fulltext']}),
    ]

class UpdateAdmin(admin.ModelAdmin):
    search_fields = ["title", "description"]
    fields = ["title", "description", "project", "url"]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Update, UpdateAdmin)
