from django.contrib import admin
from .models import Project, Post

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Post, PostAdmin)