from django import forms
from users.models import UserProfile


class LoginForm(forms.Form):
    """
    用户登录
    """
    username = forms.CharField(required=True, min_length=5, max_length=16, error_messages={
        'required': u'请输入用户名',
        'mim_length': u'用户名最少5个字符',
        'max_length': u'用户名最多16个字符'
    })
    password = forms.CharField(required=True, min_length=8, max_length=20, error_messages={
        'required': u'请输入密码',
        'min_length': u'密码最少8个字符',
        'max_length': u'密码最多20个字符'
    })


class RegisterForm(forms.Form):
    """
    用户注册
    """
    username = forms.CharField(required=True, initial=u'用户名', min_length=5, max_length=16, error_messages={
        'required': u'请输入用户名',
        'min_length': u'用户名最少5个字符',
        'max_length': u'用户名最多16个字符'
    })
    email = forms.EmailField(required=True, initial=u'正确的邮箱地址', error_messages={
        'required': u'请输入邮箱',
        'invalid': u'请输入正确的邮箱地址'
    })
    password = forms.CharField(required=True, min_length=8, max_length=20, error_messages={
        'required': u'密码不能为空哦',
        'min_length': u'密码最少8个字符',
        'max_length': u'密码最多20个字符'
    }, widget=forms.PasswordInput)
    two_password = forms.CharField(required=True, min_length=8,max_length=20, error_messages={
        'required': u'密码不能为空哦',
        'min_length': u'密码长度不能小于8位哦'
    }, widget=forms.PasswordInput(attrs={'placeholder': u'与上面密码保持一致'}))


class ModifyInfoForm(forms.Form):
    """
    补充昵称和号码及修改邮箱
    """
    nick_name = forms.CharField(max_length=20)
    mobile = forms.CharField(max_length=11)
    email = forms.EmailField()


class UserImgUploadForm(forms.ModelForm):
    """
    修改用户头像
    """
    class Meta:
        model = UserProfile
        fields = ['avatar']


class UserNameUpdateForm(forms.Form):
    """
    修改用户名
    """
    username = forms.CharField(required=True, initial=u'用户名', min_length=5, max_length=16, error_messages={
        'required': u'请输入用户名',
        'min_length': u'用户名最少5个字符',
        'max_length': u'用户名最多16个字符'
    })


class UserPasswordUpdateForm(forms.Form):
    """"
    修改用户密码
    """
    old_password = forms.CharField(required=True, min_length=8, max_length=20, error_messages={
        'required': u'密码不能为空哦',
        'min_length': u'密码最少8个字符',
        'max_length': u'密码最多20个字符'
    }, widget=forms.PasswordInput(attrs={'placeholder': u'密码错误！'}))
    new_password = forms.CharField(required=True, min_length=8, max_length=20, error_messages={
        'required': u'密码不能为空哦',
        'min_length': u'密码最少8个字符',
        'max_length': u'密码最多20个字符'
    }, widget=forms.PasswordInput)
    two_new_password = forms.CharField(required=True, min_length=8, max_length=20, error_messages={
        'required': u'密码不能为空哦',
        'min_length': u'密码长度不能小于8位哦'
    }, widget=forms.PasswordInput(attrs={'placeholder': u'与上面密码保持一致'}))