# -*- coding = utf-8 -*-
from django.shortcuts import render


def live(request):
    return render(request, 'live.html')