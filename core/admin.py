from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin View for Profile"""

    list_display = (
        'owner',
        'score',
        'highest_streak',
        'created_at',
        'updated_at',
    )
    search_fields = ['owner__username']
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (
            None,
            {
                'fields': ('owner', 'image'),
            },
        ),
        (
            'Game Stats',
            {
                'fields': ('score', 'highest_streak'),
            },
        ),
        (
            'Timestamps',
            {
                'fields': ('created_at', 'updated_at'),
                'classes': ('collapse',),
            },
        ),
    )
