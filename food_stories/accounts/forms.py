from django import forms
# from accounts.tools.validators import validate_phone_num
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'confirm password'
            }),)

    class Meta:
        model = User
        # fields = '__all__'
        fields = (
            'username',
            'email',
            'password',
            'confirm_password',
            'first_name',
            'last_name',
            'image',
            'bio',
        )
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('username')
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _('Email')
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': _('Password')
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('first name')
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('last name')
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': _('biography')
            }),
        }



# class RegisterForm(forms.Form):
#     username = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField()
#     confirm_password = forms.CharField()
#     phone_number = forms.CharField(validators=[validate_phone_num,])

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirm_password')
#         if confirm_password != password:
#             raise forms.ValidationError('confirm_password ve password eyni deyil')
#         return cleaned_data

    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data.get('phone_number')
    #     if not phone_number.startswith('+994'):
    #         raise forms.ValidationError('+994 ile baslamalidir')