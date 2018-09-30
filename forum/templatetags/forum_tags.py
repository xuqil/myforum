from django import template
from django.utils import safestring
from django.shortcuts import HttpResponse


from ..models import TopicTag, Topic
from operation.models import TopicComment, UserFavorite
from users.models import UserProfile
from operation.utils import transform_list

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


def process_menu_data(pk):
    topic = Topic.objects.filter(id=int(pk)).first()
    if not topic:
        return HttpResponse("<h1>资源不存在!</h1>")
    comment_list = list(topic.topiccomment_set.all().values('nid', 'content', 'user__username', 'parent_id_id', 'add_time'))
    comment_list = transform_list(comment_list)
    return comment_list


def produce_html(comment_list):
    html = ''
    tpl1 = """        
         <div class="comment_item">
           <div class="comment-header">
               <a href="#"><span class="user_name">{0}</span></a>
                <span class="comment_time">{1}</span>
                <span class="comment_content">{2}</span>
                <span id="{3}" hidden></span>
                <a class="reply">回复</a>
            </div>
           <div class="comment-body">{4}</div>
        </div>
           """
    for item in comment_list:
        if item['children_contents']:
            html += tpl1.format(item['user__username'], str(item['add_time'])[:19], item['content'].strip(), item['nid'],
                                produce_html(item["children_contents"]))
        else:
            html += tpl1.format(item['user__username'], str(item['add_time'])[:19], item['content'].strip(),  item['nid'], '')

    return html


from django.utils import safestring


# 引入菜单标签到模板中
@register.simple_tag
def user_comment(pk):
    # 1. 判断用户是否登录,即查看有没有权限列表
    # 2. 若为登录用户,则调动自定义函数从数据库取到菜单相关的数据
    data = process_menu_data(pk)
    # 3. 生成html, 注意转换成可以渲染的html
    html = safestring.mark_safe(produce_html(data))
    return html

