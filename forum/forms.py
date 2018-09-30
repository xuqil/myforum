from django import forms
from .models import Topic


class PubTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'content']


class TopicUpdateForm(forms.ModelForm):
    """
    话题修改表
    """
    class Meta:
        model = Topic
        fields = ['title', 'content', 'tags']
