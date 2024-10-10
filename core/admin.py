from django.contrib import admin

from .models import Game, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin view for the Profile model."""

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


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """Admin view for the Game model."""

    list_display = (
        'player',
        'score',
        'words_attempted',
        'words_correct',
        'difficulty',
        'streak',
        'date_played',
    )
    list_filter = ('difficulty', 'date_played')
    search_fields = ['player__username']
    readonly_fields = ('date_played',)

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'player',
                    'score',
                    'words_attempted',
                    'words_correct',
                ),
            },
        ),
        (
            'Game Details',
            {
                'fields': ('time_played', 'difficulty', 'streak'),
            },
        ),
        (
            'Timestamp',
            {
                'fields': ('date_played',),
                'classes': ('collapse',),
            },
        ),
    )
