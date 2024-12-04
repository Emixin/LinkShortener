from django.urls import path
from . import views


urlpatterns = [
    path('link/', views.CreateorUpdateLinkView.as_view(), name='shortened_link'),
]
