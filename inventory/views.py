from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,FormView
from django.urls import reverse_lazy
from .forms import InvPostForm,ContactForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import inv_Post
from django.core.mail import EmailMessage
from django.contrib import messages

class IndexView(TemplateView):
    template_name = 'index.html'
    
@method_decorator(login_required,name='dispatch')
class CreateInvView(CreateView):
    form_class = InvPostForm
    template_name = 'post_Inv.html'
    success_url = reverse_lazy('inventory:post_done')
    def form_valid(self, form) -> HttpResponse:
        postdate = form.save(commit=False)
        postdate.user = self.request.user
        postdate.save()
        return super().form_valid(form)
    
class PostSuccessView(TemplateView):
    template_name ='post_success.html'

class ReadingView(ListView):
    model = inv_Post
    template_name = 'reading.html'

class ContactView(FormView):
    template_name ='contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('inventory:contact')
      
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ: {}'.format(title)
        message = '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}'.format(name, email, title, message)
        from_email = 'mro2323404@stu.o-hara.ac.jp'
        to_list = ['zhaitengy006@gmail.com']
        message = EmailMessage(subject=subject,body=message,from_email=from_email,to=to_list,)
        message.send()
        messages.success(self.request, 'お問い合わせは正常に送信されました。')
        return super().form_valid(form)
