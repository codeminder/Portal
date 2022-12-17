from django.urls import path
from .views import index, dasboard


urlpatterns = [
    path("", dasboard, name = "dasboard_cashagenda"),
    path("index.html", index, name = "home_cashagenda")
]