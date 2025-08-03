from django.urls import path
#from . import views
from pages.views import IndexView, AboutView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
    # path(route, views, opt(kısayol ismi)),
]