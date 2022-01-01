from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': "name",
        }),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': "email",
        }),
    )
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': "subject",
        }),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': "message",
        }),
    )

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = 'お問合せがありました'
        message = '名前:{name}\n' \
                  'メール:{email}\n' \
                  '件名:{subject}\n' \
                  '問い合わせ内容:\n' \
                  '{message}\n'.format(name=name,
                                       email=email,
                                       subject=self.cleaned_data['subject'],
                                       message=self.cleaned_data['message'])
        from_email = '{name} <{email}>'.format(name=name, email=email)
        recipient_list = [settings.EMAIL_HOST_USER]
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")