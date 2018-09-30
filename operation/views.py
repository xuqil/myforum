from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

from .forms import CommentForm
from .models import TopicComment, UserFavorite
from forum.models import Topic
from users.models import UserProfile


def comment(request, pk):
    """
    发表评论
    """
    topic = Topic.objects.get(id=pk)
    login_user = UserProfile.objects.get(username=request.user.username)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        content = comment_form.cleaned_data['content']
        topic_comment = TopicComment()
        topic_comment.user = login_user
        topic_comment.topic = topic
        topic_comment.content = content
        topic_comment.save()
    return redirect(to='forum:detail', pk=pk)


def favorite_topics(request, pk):
    """
    :param request: 收藏者
    :return: 被收藏的主题id
    """
    fav_topic_id = pk
    user = request.user
    fav_records = UserFavorite.objects.filter(user=user, fav_id=fav_topic_id)
    if fav_records:
        fav_records.delete()
        return redirect(to='forum:detail', pk=pk)
    else:
        user_fav = UserFavorite()
        user_fav.fav_id = fav_topic_id
        user_fav.user = user
        user_fav.save()
        return redirect(to='forum:detail', pk=pk)


def user_comment(request):
    """直接在前端操作评论内容"""
    user_id = request.user.pk
    topic_id = request.POST.get("topic_id")
    comment_content = request.POST.get("comment_content").strip()
    # 若评论内容为空,则不添加任何信息
    if not comment_content:
        return HttpResponse('noy ok')

    # 1. 查看是否是通过回复(有父评论)发送还是直接评论发送
    if request.POST.get("parent_comment_id"):
        # 2. 获取该评论的父级评论id并保存记录
        c = int(request.POST.get("parent_comment_id"))
        comment_obj = TopicComment.objects.create(
            topic_id=topic_id,
            content=comment_content,
            user_id=user_id,
            parent_id_id=c
        )
    else:
        comment_obj = TopicComment.objects.create(
            topic_id=topic_id,
            content=comment_content,
            user_id=user_id
        )

    # 只传输创建时间过去
    response_ajax = {
        "comment_add_time": str(comment_obj.add_time)[:16],
        'comment_id': comment_obj.nid
    }  # 很关键,不取毫秒!
    return HttpResponse(json.dumps(response_ajax), content_type='application/json')
