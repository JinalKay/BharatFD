from django.urls import path, re_path
from .views import faq_list, index

urlpatterns = [
    path('faqs/', faq_list, name='faq-list'),
    re_path(r'^.*$', index),
]