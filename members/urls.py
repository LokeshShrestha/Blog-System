from django.urls import path
from . import views
app_name = "members"
urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/",views.login_user, name = "login"),
    path("logout/",views.logout_user, name = "logout"),
    path("profile/", views.profile, name="profile"),
    path("info/",views.infouser, name = "info")
]