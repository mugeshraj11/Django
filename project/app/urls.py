from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.InsertPageView,name="insertpage"),
    path("insert/",views.InsertData,name="insert"),
    path("showpage/",views.ShowData,name="show"),
]
