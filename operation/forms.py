from django import forms
from .models import TopicComment


class CommentForm(forms.ModelForm):
    """
    评论表
    """
    class Meta:
        model = TopicComment
        fields = ['content']