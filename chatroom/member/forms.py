import django
from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class UserSignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_update_fields = ('password1', 'password2')
        for field in class_update_fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = User
        fields = (
            'username',
            'nickname',
            'password1',
            'password2',
        )
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class LoginForm(forms.Form):
    """
    is_valid()에서 주어진 username/password를 사용한 authenticate실행
    성공시 login(request)메서드를 사용할 수 있음
    """
    username = forms.CharField(
        widget=forms.TextInput
    )
    password = forms.CharField(
        widget=forms.PasswordInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        self.user = authenticate(username=username, password=password)
        if not self.user:
            raise forms.ValidationError('Invalid login credentials')
        else:
            setattr(self, 'login', self._login)

    def _login(self, request):
        """
        django.contrib.auth.login(request)를 실행

        :param request: django.contrib.auth.login()에 주어질 HttpRequest객체
        :return: None
        """
        return django.contrib.auth.login(request, self.user)
