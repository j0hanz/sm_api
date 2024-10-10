from django.http import HttpResponse
from django.urls import path


def dummy_view(request):
    return HttpResponse('Hello World!')


urlpatterns = [
    path('', dummy_view),
]
