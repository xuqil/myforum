from django.contrib import admin
from .models import TopicComment, UserFavorite


class TopicCommentAdmin(admin.ModelAdmin):
    list_filter = ['user', 'topic', 'add_time']


admin.site.site_header = '技术小玩家论坛管理'
admin.site.site_title = '技术小玩家'
admin.site.register(TopicComment, TopicCommentAdmin)
admin.site.register(UserFavorite)
