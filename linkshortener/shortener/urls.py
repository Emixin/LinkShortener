from django.urls import path
from . import views


urlpatterns = [
    path('link/', views.CreateorUpdateLinkView.as_view(), name='shortened_link'),
    path('s/<str:code>', views.ShortLinkView.as_view(), name='short_link_view'),
    path('views/<str:code>', views.ViewsDetail.as_view(), name='view_detail'),
]
