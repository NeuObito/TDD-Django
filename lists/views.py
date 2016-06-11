from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpRequest
# Create your views here.
# You can write view here


def home_page(request):
    return render(request, 'home.html')


def test_home_page_returns_correct_html(self):
    request = HttpRequest()
    response = home_page(request)
    expected_html = render_to_string('home.html')
    self.assertEqual(response.content.decode(), expected_html)
