from django import forms
from accounts.tools.validators import validate_phone_num


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    confirm_password = forms.CharField()
    phone_number = forms.CharField(validators=[validate_phone_num,])

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if confirm_password != password:
            raise forms.ValidationError('confirm_password ve password eyni deyil')
        return cleaned_data

    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data.get('phone_number')
    #     if not phone_number.startswith('+994'):
    #         raise forms.ValidationError('+994 ile baslamalidir')
