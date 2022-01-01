from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm


class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('thanks')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ThanksView(TemplateView):
    template_name = 'thanks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "お問合せありがとうござます。"
        return context