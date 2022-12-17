from django.shortcuts import render

from .utils import DataMixin

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, "cashagenda/index.html")

def dasboard(request):
    return render(request, "cashagenda/base.html")

class LoginUser(DataMixin, LoginView):

    form_class = AuthenticationForm 
    template_name = 'cashagenda/login.html'

    def get_context_data (self, *, object_list=None, **kwargs): 
        context = super().get_context_data (**kwargs) 
        c_def = self.get_user_context(title="Authorization") 
        return dict(list(context.items()) + list(c_def.items()))
