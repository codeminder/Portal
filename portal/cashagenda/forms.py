from django.contrib.auth.forms import AuthenticationForm

class LoginUserForm(AuthenticationForm):
    error_css_class = "text-danger"