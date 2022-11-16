from .forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class SingUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/singup.html'
    success_url = reverse_lazy('login')
