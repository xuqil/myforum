from django.db import models
from users.models import UserProfile
from forum.models import Topic

from ckeditor.fields import RichTextField


class TopicComment(models.Model):
    """
    评论
    """
    nid = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name=u"主题")
    content = RichTextField(verbose_name=u"评论内容", config_name='my_cfg')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")
    parent_id = models.ForeignKey('TopicComment', verbose_name=u"子评论内容", blank=True, null=True,
                                  related_name='c_comment', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-add_time']
        verbose_name = u"用户主题评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class UserFavorite(models.Model):
    """
    收藏
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户", related_name='user_fav')
    fav_id = models.IntegerField(default=0, verbose_name=u"收藏的主题ID")
    add_time = models.DateTimeField(auto_now=True, verbose_name=u"收藏时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.nick_name
