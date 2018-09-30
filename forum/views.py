from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, DetailView, UpdateView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Topic, Board, TopicTag
from users.models import UserProfile
from .forms import PubTopicForm, TopicUpdateForm
from operation.forms import CommentForm
from operation.models import UserFavorite


class IndexView(ListView):
    """
    首页
    """
    template_name = 'index.html'
    context_object_name = 'topics'

    def get(self, request, *args, **kwargs):
        topic_list = Topic.objects.all().order_by('-add_time')
        paginator = Paginator(topic_list, 10)
        page = request.GET.get('page', *args, **kwargs)
        try:
            topics = paginator.page(page)
            is_paginated = 1
        except PageNotAnInteger:
            topics = paginator.page(1)
            is_paginated = 2
        except EmptyPage:
            is_paginated = 0
            topics = paginator.page(paginator.num_pages)

        if request.user.is_authenticated:
            topic_count = UserProfile.objects.get(username=request.user).topic_set.count()
            return render(request, self.template_name, {
                'topics': topics,
                'topic_count': topic_count,
                'paginator': paginator,
                'is_paginated': is_paginated
            })
        else:
            return render(request, self.template_name, {
                'topics': topics,
                'paginator': paginator,
                'is_paginated': is_paginated
            })


class TopicDetailView(DetailView):
    """
    主题详情
    """
    model = Topic
    template_name = 'forum/detail.html'
    context_object_name = 'topic'

    def get(self, request, *args, **kwargs):
        response = super(TopicDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        topic = super(TopicDetailView, self).get_object(queryset=None)
        return topic

    def get_context_data(self, **kwargs):
        comment_form = CommentForm()
        topic_comment = self.object.topiccomment_set.all().order_by('-add_time')
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context.update({
            'comment_form': comment_form,
            'topic_comment': topic_comment,
            'user': self.object.user,
        })
        return context


def pub_topic(request, username, pk):
    """
    发布主题
    """
    tags = TopicTag.objects.all()
    user = UserProfile.objects.get(username=username)
    topic_form = PubTopicForm()
    return render(request, 'forum/edit.html', {
        'topic_form': topic_form,
        'user': user,
        'board_id': pk,
        'tags': tags,
    })


def commit_topic(request, username, board_id):
    """
    提交主题
    """
    topic_form = PubTopicForm(request.POST)
    board = get_object_or_404(Board, pk=board_id)
    tags = TopicTag.objects.all()
    if topic_form.is_valid():
        topic_title = topic_form.cleaned_data['title']
        topic_content = topic_form.cleaned_data['content']
        topic_tags = request.POST.getlist('tags')
        if Topic.objects.filter(title=topic_title).exists():
            return render(request, 'forum/edit.html', {
                'msg': '主题已存在',
                'topic_form': topic_form,
                'board_id': board_id,
                'tags': tags,
                'exists': Topic.objects.filter(title=topic_title).exists()
            })
        topic = Topic()
        user = UserProfile.objects.get(username=username)
        topic.user = user
        topic.title = topic_title
        topic.content = topic_content
        topic.boards = board
        topic.save()
        # 注意标签的关联为topic保存之后
        for tag in topic_tags:
            topic.tags.add(tag)
        return render(request, 'forum/edit.html', {
            'topic_form': topic_form,
            'msg': '提交成功',
            'board_id': board_id,
            'tags': tags,
        })
    else:
        return render(request, 'forum/edit.html', {
            'msg': '输入数据有错误，请重新输入！',
            'topic_form': topic_form,
            'board_id': board_id,
            'tags': tags,
        })


class BoardsView(ListView):
    """
    板块
    """
    model = Board
    template_name = 'forum/boards.html'
    context_object_name = 'boards'


class BoardDetailView(ListView):
    """
    某包含具体主题的板块
    """
    model = Topic
    template_name = 'forum/board_detail.html'
    context_object_name = 'topics'
    paginate_by = 10  # 开启分页功能

    def get_queryset(self):
        board = get_object_or_404(Board, pk=self.kwargs.get('pk'))
        return super(BoardDetailView, self).get_queryset().filter(boards=board)


def topic_delete(request, pk):
    """
    删除主题
    """
    topic_id = pk
    Topic.objects.filter(id=topic_id).delete()
    return redirect(to='forum:index')


class TopicUpdateView(UpdateView):
    """
    修改主题
    """
    model = Topic
    form_class = TopicUpdateForm
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        topic = form.save(commit=False)
        topic.save()
        topic_detail_url = reverse('forum:detail', kwargs={'pk': topic.pk})
        return redirect(topic_detail_url)


class TagsView(ListView):
    """
    具体标签下的主题
    """
    model = Topic
    template_name = 'forum/tag_detail.html'
    context_object_name = 'topics'
    paginate_by = 10  # 开启分页功能

    def get_queryset(self):
        tag = get_object_or_404(TopicTag, pk=self.kwargs.get('pk'))
        return super(TagsView, self).get_queryset().filter(tags=tag)

    def get_context_data(self, **kwargs):
        tag = get_object_or_404(TopicTag, pk=self.kwargs.get('pk'))
        context = super(TagsView, self).get_context_data(**kwargs)
        context.update({
            'tag': tag
        })
        return context


class UserTopicsView(ListView):
    """
    用户下的主题
    """
    model = Topic
    template_name = 'forum/user_topics.html'
    context_object_name = 'topics'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(UserProfile, pk=self.kwargs.get('pk'))
        return super(UserTopicsView, self).get_queryset().filter(user=user)
