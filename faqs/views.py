from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FAQ
from .serializers import FAQSerializer
from django.views.generic import TemplateView
from django.shortcuts import render
import os

def index(request):
    # Adjust the path according to where your build folder is located
    return render(request, os.path.join("frontend_build", "index.html"))

@api_view(['GET'])
def faq_list(request):
    lang = request.GET.get('lang', 'en')
    faqs = FAQ.objects.all()
    data = [
        {
            'id': faq.id,
            'question': faq.get_translated_question(lang),
            'answer': faq.answer,
        } for faq in faqs
    ]
    return Response(data)