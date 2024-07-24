from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit


def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    page_title = {
        "page_title": "Home",
        "page_visit_count": queryset.count()
    }
    PageVisit.objects.create()
    return render(request, 'home.html', page_title)