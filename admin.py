from django.contrib import admin
from link_manager.models import Link, LinkOpened


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    # list_display = ('id', 'full_url', 'created_at', 'updated_at')
    # search_fields = ('full_url',)
    list_display = ('id', 'full_url')
    pass

@admin.register(LinkOpened)
class LinkOpenedAdmin(admin.ModelAdmin):
    # list_display = ('id', 'link', 'profile', 'created_at', 'updated_at')
    # search_fields = ('link__full_url', 'profile__user__username')
    # list_filter = ('profile__user__username',)    
    list_display = ('id', )
    pass