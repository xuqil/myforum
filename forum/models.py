from django.db import models
from users.models import UserProfile

from ckeditor.fields import RichTextField


class TopicTag(models.Model):
    """
    主题标签
    """
    name = models.CharField(max_length=100, verbose_name=u"标签名")

    class Meta:
        verbose_name = u"主题标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Board(models.Model):
    """
    主题板块
    """
    name = models.CharField(max_length=30, verbose_name=u"板块名称")

    class Meta:
        verbose_name = u"板块"
        verbose_name_plural = verbose_name

    @property
    def topics_count(self):
        return Topic.objects.filter(topic__board=self).count()

    @property
    def last_post(self):
        return Topic.objects.filter(topic__board=self).order_by('add_time').first()

    def __str__(self):
        return self.name


class Topic(models.Model):
    """
    用户主题
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户|")
    title = models.CharField(max_length=100, verbose_name=u"标题")
    content = RichTextField(verbose_name=u"主题内容", config_name='my_cfg')
    boards = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE,
                               verbose_name=u"论坛", default=u"Python")
    tags = models.ManyToManyField(TopicTag, blank=True)
    views = models.PositiveIntegerField(default=0, verbose_name=u"阅读次数")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"主题"
        verbose_name_plural = verbose_name
        # 排序
        ordering = ['-add_time']

    def __str__(self):
        return self.title

    # 阅读量加一
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])