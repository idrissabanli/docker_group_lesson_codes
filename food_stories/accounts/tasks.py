from django.contrib.auth import get_user_model
from accounts.tools.token import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.core.mail import EmailMessage

User = get_user_model()

def send_confirmation_email(user_id, site_address):
    user = User.objects.get(pk=user_id)
    mail_subject = _('Activate your account')
    template = 'email/confirmation_email.html'
    token = account_activation_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    redirect_url = reverse_lazy('activation', kwargs = {
        'uidb64': uid,
        'token': token,
    })
    message = render_to_string(template, {
            'user': user,
            'redirect_url': f"http://{site_address}{redirect_url}",
        })
    email = EmailMessage(
            mail_subject, message, to=[user.email]
        )
    email.content_subtype = 'html'
    email.send()