from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit


def home_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    queryset = PageVisit.objects.all()
    page_title = {
        "page_title": "Home",
        "page_visit_count": page_qs.count(),
        "percent": (page_qs.count() * 100.0) / qs.count(),
        "total_visit_count": qs.count(),
    }
    PageVisit.objects.create()
    return render(request, 'home.html', page_title)


def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent = (page_qs.count() * 100.0) / qs.count()
    except:
        percent = 0

    page_title = {
        "page_title": "Home",
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visit_count": qs.count(),
    }
    PageVisit.objects.create()
    return render(request, 'home.html', page_title)