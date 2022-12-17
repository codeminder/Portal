from django.urls import path
from .views import LoginUser, index, dasboard


urlpatterns = [
    path("", dasboard, name = "dasboard_cashagenda"),
    path("index.html", index, name = "home_cashagenda"),
    path("login/", LoginUser.as_view(), name = "login_cashagenda")
]