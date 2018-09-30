from django import template

from ..models import TopicTag, Topic
from operation.models import TopicComment
from users.models import UserProfile

register = template.Library()


@register.simple_tag()
def get_got_topics():
    """
    获取热议主题话题
    :return:前8个热议主题
    """
    hot_topics = Topic.objects.all().order_by("-views")[:8]
    return hot_topics


@register.simple_tag()
def get_tags():
    """
    获取标签
    :return: 标签
    """
    return TopicTag.objects.all()


@register.simple_tag()
def get_topics_count():
    """
    获取主题数
    :return: 主题数
    """
    return Topic.objects.count()


@register.simple_tag()
def get_comments_count():
    """
    获取总评论数
    :return:主题回复数
    """
    return TopicComment.objects.count()


@register.simple_tag()
def get_users_count():
    """
    获取用户注册数
    :return: 用户注册数
    """
    return UserProfile.objects.count()
