from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .models import StaticPage

class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = StaticPage.objects.all()
        return context

class AdminPageView(LoginRequiredMixin, TemplateView):
    template_name = 'admin_page.html'

class AdminPageView(TemplateView):
    template_name = 'admin_page.html'

@login_required
def restricted_page(requests):
    return render(requests, 'restricted_page.html')








