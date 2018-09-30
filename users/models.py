from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=20, verbose_name=u"昵称", default="")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"电话")
    avatar = models.ImageField(upload_to="image/users/%Y/%m", default=u"image/default.png",
                               max_length=100, verbose_name=u"头像")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
