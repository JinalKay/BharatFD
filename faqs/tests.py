import pytest
from rest_framework.test import APIClient
from .models import FAQ

@pytest.mark.django_db
def test_faq_list():
    FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")
    client = APIClient()
    response = client.get('/api/faqs/?lang=hi')
    assert response.status_code == 200
    assert 'question' in response.data[0]