
from django.urls import path,include
from . import views

urlpatterns=[
    path("",views.IndexPage,name="index"),
    path("signup/",views.SignupPage,name="signup",
    )
]
