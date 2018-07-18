from django.contrib import admin
from .models import LikeCount, LikeRecord


@admin.register(LikeCount)
class LikeCountAdmin(admin.ModelAdmin):
    list_display = (
        'content_type', 'object_id', 'content_object', 'liked_num',)


@admin.register(LikeRecord)
class LikeRecordAdmin(admin.ModelAdmin):
    list_display = (
        'content_type', 'object_id', 'content_object', 'liked_time', 'user',)
